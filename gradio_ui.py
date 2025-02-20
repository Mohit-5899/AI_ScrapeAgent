import gradio as gr
from agent import run_agent

def scrape_with_ai(url, method):
    """Function that takes a URL & selected method to return the AI-generated summary."""
    if not url.startswith("http"):
        return "⚠️ Please enter a valid URL starting with http or https."

    try:
        result = run_agent(url, method)
        return result
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Create a Gradio interface with dropdown selection
with gr.Blocks() as demo:
    gr.Markdown("## 🌐 AI Web Scraper - Choose Your Scraping Method")
    gr.Markdown("Enter a website URL and select a scraping method.")

    url_input = gr.Textbox(label="Website URL", placeholder="Enter URL here...")
    method_dropdown = gr.Dropdown(
        ["Normal", "Firecrawl", "Crawl4AI"], label="Choose Scraping Method"
    )
    result_output = gr.Textbox(label="Scraped Summary", interactive=False)

    submit_button = gr.Button("🔍 Scrape Website")

    submit_button.click(fn=scrape_with_ai, inputs=[url_input, method_dropdown], outputs=result_output)

# Run Gradio UI
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860, share=True)
