# Crawl4AI + MCP Pipeline

🚀 A complete, production-grade system for smart web crawling, AI-driven content processing, and structured data storage — with zero architecture guesswork!

---

## 📦 Project Structure

```
crawl4ai-mcp/
├─ 01_Crawl4AI_Scraper/          # Python scraper + helper modules
│   ├─ crawler.py
│   ├─ parser.py
│   └─ requirements.txt
├─ 02_MCP_Modules/               # AI JSON modules (M1-M6)
│   ├─ m1-extract-urls.json
│   ├─ m2-fetch-content.json
│   ├─ m3-clean-html.json
│   ├─ m4-summarize.json
│   ├─ m5-extract-entities.json
│   └─ m6-format-output.json
├─ 03_Integration/               # n8n workflow export & connector
│   ├─ n8n_workflow.json
│   └─ connector.js
├─ 04_Logging/                   # Centralized logger
│   └─ logger.py
├─ config/                       # Configuration and environment settings
│   ├─ config.example.json
│   └─ .env
└─ README.md                     # Project guide
```

---

## ⚡ Quick Start

### 1. Clone the repository (if needed)
```bash
git clone https://github.com/your-repo/crawl4ai-mcp.git
cd crawl4ai-mcp
```

### 2. Setup Python environment
```bash
cd 01_Crawl4AI_Scraper/
pip install -r requirements.txt
playwright install
```

---

### 3. Configure your project
- Copy `config/config.example.json` to `config/config.json`.
- Update your real API keys, URLs, rate limits.
- Fill `.env` file with your secrets (OpenAI, SerpAPI, Google Sheets, etc.).

---

### 4. Run the crawler manually (optional test)
```bash
python crawler.py
```
✅ Output will be saved in `/output/cleaned_pages.json`.

---

### 5. Setup and run n8n

Install and start n8n:
```bash
npm install -g n8n
n8n start
```

- Open browser: [http://localhost:5678](http://localhost:5678)
- Import `03_Integration/n8n_workflow.json`
- Connect nodes and add your credentials (Google Sheets, OpenAI, etc.)
- Trigger the workflow!

---

## 📈 Advanced Setup

- Setup Prometheus and Grafana for monitoring.
- Deploy using Docker and Kubernetes if scaling is needed.
- Migrate storage from Google Sheets ➔ Azure CosmosDB ➔ Pinecone/Weaviate (semantic search).

---

## 🛡️ Security Best Practices

- Store your `.env` securely.
- Never commit API keys to GitHub.
- Use Vault / AWS Secrets Manager in production.

---

## 📑 Documentation Links
- [n8n Documentation](https://docs.n8n.io/)
- [Playwright Python](https://playwright.dev/python/)
- [OpenAI API Docs](https://platform.openai.com/docs/)
- [Pinecone Docs](https://docs.pinecone.io/)

---

## 👨‍💻 About
Built with ❤️ for intelligent, scalable, AI-powered web crawling and data extraction.
