'''
🟦 DuckDuckGoSearchRun
Returns: A single string summary of top search results.
Purpose: Quick, simple answer.
Use Case: When you want a readable response directly usable by an LLM.

XX
🟨 DuckDuckGoSearchResults
Returns: A list of detailed search results (dicts with title, link, snippet, etc.).
Purpose: Structured result format, for tools, parsing, or custom rendering.
Use Case: When you want to display or process multiple search result entries.

'''

from langchain_community.tools import DuckDuckGoSearchResults
from langchain_community.utilities.duckduckgo_search import DuckDuckGoSearchAPIWrapper

# Create a custom wrapper
custom_wrapper = DuckDuckGoSearchAPIWrapper(
    region="wt-wt",           # Worldwide
    max_results=10,            # Limit number of search results
    backend="api" ,
    source = 'news'           # Optional: "lite", "html", or "api" (faster/simpler responses)
)

# Instantiate the search tool
search_tool = DuckDuckGoSearchResults(api_wrapper=custom_wrapper)

# Define your query
query = "Berlin startup news"

# Perform the search
results = search_tool.invoke(query)

# Display the results
print(results)

