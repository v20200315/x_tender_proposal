from typing import List, TypedDict

from langchain_core.documents import Document


class GraphState(TypedDict):
    """
    Represents the state of our graph.
    """

    paths: List[str]
    min_length: int
    project_name: str
    input_texts: List[str]
    web_search_queries: List[str]
    documents: List[Document]
    section_path: str
