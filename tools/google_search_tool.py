import os
from langchain.tools.tavily_search import TavilySearchResults

search_tool = TavilySearchResults(api_key=os.getenv("TAVILY_API_KEY"))
