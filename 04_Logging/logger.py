# crawl4ai-mcp/04_Logging/logger.py

import logging
import os
from datetime import datetime

# Create logs directory if it doesn't exist
os.makedirs("../logs", exist_ok=True)

# Configure logging
logging.basicConfig(
    filename=f"../logs/crawl4ai_{datetime.now().strftime('%Y%m%d')}.log",
    filemode="a",
    format="%(asctime)s | %(levelname)s | %(module)s | %(message)s",
    level=logging.INFO
)

def get_logger(name):
    """Create a custom logger with a module name."""
    logger = logging.getLogger(name)
    return logger

# Example usage (remove/comment after testing):
if __name__ == "__main__":
    log = get_logger("TestLogger")
    log.info("Logger initialized successfully.")
    log.warning("This is a test warning.")
    log.error("This is a test error.")
