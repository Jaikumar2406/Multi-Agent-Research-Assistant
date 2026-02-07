from duckduckgo_search import DDGS
def duckduckgo_search(query):
    """
    Searches the web using DuckDuckGo and returns top organic results including titles and URLs.
    """
    data = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=5):
            data.append({
                "title": r["title"],
                "url": r["href"]
            })
    return data