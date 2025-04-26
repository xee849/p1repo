// crawl4ai-mcp/03_Integration/connector.js

const axios = require('axios');
require('dotenv').config();

async function crawlUrl(url) {
  try {
    const response = await axios.post('http://localhost:8000/fetch', { url });
    console.log("Fetched content:", response.data);
  } catch (error) {
    console.error("Error:", error.message);
  }
}

const testUrl = process.argv[2];
if (!testUrl) {
  console.log("Usage: node connector.js <url>");
  process.exit(1);
}

crawlUrl(testUrl);