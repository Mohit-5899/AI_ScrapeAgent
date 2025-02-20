# AI Web Scraping Agent

An intelligent web scraping agent that uses multiple scraping methods and LangChain for content analysis.

## Features

- Multiple scraping methods:
  - Normal: Traditional web scraping using Playwright & BeautifulSoup
  - Firecrawl: Advanced scraping with JavaScript support
  - Crawl4AI: AI-powered content extraction
- Interactive UI using Gradio
- Content summarization using GPT-4
- Automatic fallback mechanism

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/AI_ScrapeAgent.git
cd AI_ScrapeAgent
```

2. Create a virtual environment:
```bash
python -m venv scrapvenv
source scrapvenv/bin/activate  # On Windows: scrapvenv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file with your API keys:
```
OPENAI_API_KEY=your_openai_key
FIRECRAWL_API_KEY=your_firecrawl_key
```

## Usage

1. Run the Gradio UI:
```bash
python gradio_ui.py
```

2. Or use the command line interface:
```bash
python main.py
```

## Project Structure

- `agent.py`: LangChain agent implementation
- `scraper.py`: Web scraping methods implementation
- `tools.py`: LangChain tools definition
- `main.py`: Command-line interface
- `gradio_ui.py`: Gradio web interface

## Requirements

- Python 3.8+
- See requirements.txt for full list of dependencies
