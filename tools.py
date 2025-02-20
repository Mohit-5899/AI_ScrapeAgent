from langchain.tools import Tool
from scraper import scrape_normal, scrape_firecrawl, scrape_crawl4ai

# Define different tools for each scraping method
scrape_tool_normal = Tool(
    name="Web Scraper (Normal)",
    func=scrape_normal,
    description="Scrapes text content from a webpage using Playwright & BeautifulSoup."
)

scrape_tool_firecrawl = Tool(
    name="Web Scraper (Firecrawl)",
    func=scrape_firecrawl,
    description="Scrapes data using Firecrawl AI API."
)

scrape_tool_crawl4ai = Tool(
    name="Web Scraper (Crawl4AI)",
    func=scrape_crawl4ai,
    description="Scrapes data using Crawl4AI open-source framework."
)
