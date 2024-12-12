from typing import List, TypedDict

from langchain_core.documents import Document


class GraphState(TypedDict):
    """
    Represents the state of our graph.
    """

    paths: List[str]
    input_text: str
    outline_json: str
    web_search_query: str
    documents: List[Document]
    summarization: str
    article_path: str
