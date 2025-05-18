import wikipedia

# Set the language (optional, default is "en")
wikipedia.set_lang("en")

# Search for a topic
results = wikipedia.search("Nikola Tesla")
print("Search results:", results)

# Get summary of the first result
summary = wikipedia.summary("Nikola Tesla", sentences=3)
print("\nSummary:\n", summary)

# Get full page content
page = wikipedia.page("Nikola Tesla")
print("\nTitle:", page.title)
print("\nURL:", page.url)
print("\nContent (first 1000 chars):\n", page.content[:500])
