import requests
import xml.etree.ElementTree as ET

def search_arxiv(query: str, limit: int = 5):
    """
    Search arXiv for research papers.

    Args:
        query (str): search query
        limit (int): number of papers to fetch

    Returns:
        list: list of papers with metadata
    """

    base_url = "http://export.arxiv.org/api/query"
    params = {
        "search_query": f"all:{query}",
        "start": 0,
        "max_results": limit, 
        "sortBy": "submittedDate",
        "sortOrder": "descending"
    }

    response = requests.get(base_url, params=params)
    response.raise_for_status()

    root = ET.fromstring(response.text)
    ns = {"atom": "http://www.w3.org/2005/Atom"}

    papers = []

    for entry in root.findall("atom:entry", ns):
        title = entry.find("atom:title", ns).text.strip()
        summary = entry.find("atom:summary", ns).text.strip()

        authors = [
            author.find("atom:name", ns).text
            for author in entry.findall("atom:author", ns)
        ]

        pdf_link = None
        for link in entry.findall("atom:link", ns):
            if link.attrib.get("title") == "pdf":
                pdf_link = link.attrib["href"]

        papers.append({
            "title": title,
            "authors": authors,
            "summary": summary,
            "pdf_url": pdf_link
        })

    return papers