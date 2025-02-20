import sys
from agent import run_agent

def get_scraping_method():
    """Prompts user to select a scraping method."""
    print("\nAvailable scraping methods:")
    print("1. Normal - Traditional web scraping")
    print("2. Firecrawl - Advanced scraping with JavaScript support")
    print("3. Crawl4AI - AI-powered content extraction")
    
    while True:
        choice = input("\nSelect a method (1-3) [Default: 1]: ").strip()
        if not choice:
            return "normal"
        
        method_map = {
            "1": "normal",
            "2": "firecrawl",
            "3": "crawl4ai"
        }
        
        if choice in method_map:
            return method_map[choice]
        print("Invalid choice. Please select 1, 2, or 3.")

def main():
    """Handles dynamic user input for running the AI agent."""
    if len(sys.argv) > 1:
        # Run with CLI argument
        url = sys.argv[1]
    else:
        # Prompt user for URL input
        url = input("Enter a website URL to scrape: ")
    
    # Get scraping method
    method = get_scraping_method()
    
    print(f"\n🔍 Scraping website: {url}")
    print(f"📋 Using method: {method}")
    
    result = run_agent(f"{url}|{method}")
    print("\n📄 Summary:\n", result)

if __name__ == "__main__":
    main()
