import feedparser
import urllib.parse


def google_news_search(query, max_results=5):

    """
    Fetch news from Google News RSS (FREE)
    """
    encoded_query = urllib.parse.quote(query)
    rss_url = f"https://news.google.com/rss/search?q={encoded_query}&hl=en-IN&gl=IN&ceid=IN:en"

    feed = feedparser.parse(rss_url)

    results = []
    for entry in feed.entries[:max_results]:
        results.append({
            "title": entry.title,
            "url": entry.link,
            "summary": entry.get("summary", ""),
            "source": "google_news"
        })

    return results