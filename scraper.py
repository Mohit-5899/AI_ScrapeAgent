from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import requests
import os
import asyncio
from crawl4ai import AsyncWebCrawler
from dotenv import load_dotenv
from duckduckgo_search import DDGS

# Load API keys
load_dotenv()
# Firecrawl API Key
FIRECRAWL_API_KEY = os.getenv("FIRECRAWL_API_KEY")

def scrape_normal(url: str):
    """Normal Web Scraping using Playwright & BeautifulSoup"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, timeout=60000)
        content = page.content()
        browser.close()

    soup = BeautifulSoup(content, "html.parser")
    paragraphs = [p.get_text(strip=True) for p in soup.find_all("p")]
    return {"url": url, "method": "Normal", "content": paragraphs[:10]}

def scrape_firecrawl(url: str):
    """Web Scraping using Firecrawl API"""
    if not FIRECRAWL_API_KEY:
        return {"error": "Firecrawl API Key is missing!"}

    api_url = "https://api.firecrawl.io/v1/scrape"
    headers = {
        "Authorization": f"Bearer {FIRECRAWL_API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "url": url,
        "render_js": True,
        "extract_text": True,
        "wait_for": 5000  # Wait 5 seconds for dynamic content
    }

    try:
        response = requests.post(api_url, headers=headers, json=data)
        if response.status_code == 200:
            result = response.json()
            # Extract text content from the response
            content = result.get("data", {}).get("text", [])
            if isinstance(content, str):
                content = [content]
            return {"url": url, "method": "Firecrawl", "content": content[:10]}
        else:
            error_msg = f"Firecrawl API error: Status code {response.status_code}"
            print(error_msg)
            return {"error": error_msg, "fallback": scrape_normal(url)}
    except Exception as e:
        error_msg = f"Firecrawl error: {str(e)}"
        print(error_msg)
        return {"error": error_msg, "fallback": scrape_normal(url)}

def scrape_duckduckgo(url: str):
    """Web Scraping using DuckDuckGo Search API"""
    try:
        # Extract domain from URL for searching
        domain = url.split("//")[-1].split("/")[0]
        search_query = f"site:{domain}"
        
        results = []
        with DDGS() as ddgs:
            # Get text results from DuckDuckGo
            ddg_results = ddgs.text(search_query, max_results=10)
            for r in ddg_results:
                results.append({
                    'title': r['title'],
                    'snippet': r['body'],
                    'link': r['link']
                })
        
        # Extract content from results
        content = [f"{r['title']}: {r['snippet']}" for r in results]
        return {"url": url, "method": "DuckDuckGo", "content": content}
    except Exception as e:
        error_msg = f"DuckDuckGo error: {str(e)}"
        print(error_msg)
        return {"error": error_msg, "fallback": scrape_normal(url)}

async def scrape_crawl4ai_async(url: str):
    """Web Scraping using Crawl4AI"""
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url=url)
        return {"url": url, "method": "Crawl4AI", "content": result.markdown}

def scrape_crawl4ai(url: str):
    """Wrapper function to run Crawl4AI synchronously"""
    return asyncio.run(scrape_crawl4ai_async(url))
