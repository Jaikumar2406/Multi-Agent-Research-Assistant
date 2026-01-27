import requests

def search_wikipedia(query: str, limit: int = 5):
    """
    Fetch summaries from Wikipedia based on a query.

    Args:
        query (str): search topic
        limit (int): number of responses to fetch

    Returns:
        list: list of summaries
    """

    headers = {
        "User-Agent": "AI-Research-Agent/1.0 (contact: youremail@example.com)"
    }

    search_url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "list": "search",
        "srsearch": query,
        "format": "json",
        "srlimit": limit
    }

    response = requests.get(search_url, params=params, headers=headers)
    response.raise_for_status()

    search_results = response.json()["query"]["search"]

    summaries = []

    for result in search_results:
        title = result["title"].replace(" ", "_")
        summary_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}"

        summary_resp = requests.get(summary_url, headers=headers)

        if summary_resp.status_code == 200:
            data = summary_resp.json()
            summaries.append(data.get("extract"))

    return summaries