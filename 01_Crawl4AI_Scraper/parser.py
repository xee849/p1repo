# crawl4ai-mcp/01_Crawl4AI_Scraper/parser.py

from bs4 import BeautifulSoup

def clean_html(raw_html):
    """Cleans navigation bars, footers, ads, etc."""
    soup = BeautifulSoup(raw_html, "lxml")
    
    # Remove common unwanted elements
    for selector in ["nav", "footer", ".ad", ".advertisement", "script", "style"]:
        for tag in soup.select(selector):
            tag.decompose()
    
    # Extract text
    cleaned_text = soup.get_text(separator=" ", strip=True)
    return cleaned_text
