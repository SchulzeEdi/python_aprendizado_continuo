from langchain_community.tools import TavilySearchResults

def tavily_search_tool(domains):
    return TavilySearchResults(
        max_results=5,
        include_raw_content=True,
        search_depth='advanced',
        include_domains=domains
    )