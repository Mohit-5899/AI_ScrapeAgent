import gradio as gr
from scraper import (
    scrape_normal,
    scrape_firecrawl,
    scrape_crawl4ai,
    scrape_duckduckgo
)

def process_url(url: str, method: str):
    """Process URL based on selected method"""
    try:
        if method == "Normal":
            result = scrape_normal(url)
        elif method == "Firecrawl":
            result = scrape_firecrawl(url)
        elif method == "Crawl4AI":
            result = scrape_crawl4ai(url)
        elif method == "DuckDuckGo":
            result = scrape_duckduckgo(url)
        else:
            return "Invalid method selected"

        if "error" in result:
            return f"Error: {result['error']}\nFallback result: {result.get('fallback', 'No fallback available')}"
        
        content = result.get("content", [])
        if isinstance(content, list):
            return "\n\n".join(content)
        return content
    except Exception as e:
        return f"Error: {str(e)}"

def create_ui():
    """Create Gradio interface"""
    iface = gr.Interface(
        fn=process_url,
        inputs=[
            gr.Textbox(label="URL to scrape", placeholder="Enter URL..."),
            gr.Radio(
                choices=["Normal", "Firecrawl", "Crawl4AI", "DuckDuckGo"],
                label="Scraping Method",
                value="Normal"
            )
        ],
        outputs=gr.Textbox(label="Scraped Content"),
        title="AI Web Scraping Agent",
        description="Enter a URL and choose a scraping method to extract content.",
        examples=[
            ["https://example.com", "Normal"],
            ["https://example.com", "Firecrawl"],
            ["https://example.com", "Crawl4AI"],
            ["https://example.com", "DuckDuckGo"]
        ]
    )
    return iface

if __name__ == "__main__":
    ui = create_ui()
    ui.launch()
