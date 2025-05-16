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

