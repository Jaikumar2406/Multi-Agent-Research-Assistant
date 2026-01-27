from duckduckgo_search import DDGS

def blog_search(query, max_results=5):

    """
    Fetch blog articles related to a topic using DuckDuckGo search.

    Parameters:
        query (str): Topic or keywords for blog search
        max_results (int): Number of blog results to fetch

    Returns:
        list[dict]: List of blog results with title and URL
    """
    blogs = []

    blog_query = f"{query} blog"

    with DDGS() as ddgs:
        for r in ddgs.text(blog_query, max_results=max_results):
            blogs.append({
                "title": r.get("title"),
                "url": r.get("href"),
                "source": "blog"
            })

    return blogs