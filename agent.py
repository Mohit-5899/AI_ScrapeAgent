from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory
from tools import scrape_tool_normal, scrape_tool_firecrawl, scrape_tool_crawl4ai
import os
from dotenv import load_dotenv

# Load API keys
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize AI model
llm = ChatOpenAI(temperature=0, model_name="gpt-4", openai_api_key=OPENAI_API_KEY)

# Function to run agent based on selected scraping method
def run_agent(url: str, method: str):
    """Runs the AI agent using the selected scraping method."""
    
    # Select the appropriate scraping tool
    if method == "Normal":
        tool = scrape_tool_normal
    elif method == "Firecrawl":
        tool = scrape_tool_firecrawl
    elif method == "Crawl4AI":
        tool = scrape_tool_crawl4ai
    else:
        return "❌ Invalid Scraping Method!"

    # Initialize AI agent with the selected tool
    agent = initialize_agent(
        tools=[tool],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        memory=ConversationBufferMemory(memory_key="chat_history", return_messages=True),
    )

    return agent.invoke({"input": f"Scrape the website {url} using {method} and summarize its content."})["output"]
