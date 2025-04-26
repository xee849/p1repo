# crawl4ai-mcp/01_Crawl4AI_Scraper/crawler.py

import asyncio
import httpx
from playwright.async_api import async_playwright
from parser import clean_html
import os
import json
from dotenv import load_dotenv

load_dotenv()

# Load configuration
with open(os.path.join("../config/config.json")) as f:
    config = json.load(f)

HEADERS = {"User-Agent": "Crawl4AI-MCP/1.0"}
TIMEOUT = 15

async def fetch_html(url, use_playwright=False):
    """Fetches HTML content, using Playwright if JS rendering is needed."""
    if use_playwright:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            await page.goto(url, timeout=TIMEOUT*1000)
            content = await page.content()
            await browser.close()
            return content
    else:
        async with httpx.AsyncClient(timeout=TIMEOUT) as client:
            response = await client.get(url, headers=HEADERS)
            response.raise_for_status()
            return response.text

async def process_url(url):
    """Process a single URL: fetch HTML and clean it."""
    try:
        print(f"Fetching {url}...")
        html = await fetch_html(url, use_playwright=False)
        text = clean_html(html)
        
        if len(text) < config["crawl"].get("minTextLength", 200):
            print(f"[WARNING] Very short page detected: {url}")
        
        return {
            "url": url,
            "clean_text": text
        }
    except Exception as e:
        print(f"[ERROR] Failed to fetch {url}: {str(e)}")
        return None

async def main(urls):
    """Main entrypoint."""
    tasks = [process_url(url) for url in urls]
    results = await asyncio.gather(*tasks)
    results = [r for r in results if r]
    
    # Save results to a file
    os.makedirs("../output", exist_ok=True)
    with open("../output/cleaned_pages.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    
    print(f"Processed {len(results)} pages.")

if __name__ == "__main__":
    seed_urls = config["crawl"]["seedUrls"]
    asyncio.run(main(seed_urls))
