from langchain.tools import Tool
from scraper import (
    scrape_normal,
    scrape_firecrawl,
    scrape_crawl4ai,
    scrape_duckduckgo
)

def get_scraping_tools():
    """Get all available scraping tools"""
    return [
        Tool(
            name="Normal_Scraper",
            func=scrape_normal,
            description="Scrapes a webpage using Playwright and BeautifulSoup. Use this for basic web scraping."
        ),
        Tool(
            name="Firecrawl_Scraper",
            func=scrape_firecrawl,
            description="Scrapes a webpage using Firecrawl API. Use this for advanced API-based scraping."
        ),
        Tool(
            name="Crawl4AI_Scraper",
            func=scrape_crawl4ai,
            description="Scrapes a webpage using Crawl4AI. Use this for AI-powered content extraction."
        ),
        Tool(
            name="DuckDuckGo_Scraper",
            func=scrape_duckduckgo,
            description="Scrapes website content using DuckDuckGo search. Use this for getting summarized content from a domain."
        )
    ]
