from Agents.blog_search import blog_search
from Agents.duckduck import duckduckgo_search
from Agents.google_news import google_news_search
import asyncio


async def run_all(topic):
    """Fetch web search, news and blogs in parallel for a topic."""
    queries = {
        "search": f"{topic} overview",
        "news": f"{topic} latest news",
        "blogs": f"{topic} blog tutorial"
    }

    search_res, news_res, blog_res = await asyncio.gather(
        asyncio.to_thread(duckduckgo_search, queries["search"]),
        asyncio.to_thread(google_news_search, queries["news"]),
        asyncio.to_thread(blog_search, queries["blogs"])
    )

    return {
        "search": search_res,
        "news": news_res,
        "blogs": blog_res
    }