from typing import List, TypedDict

from langchain_core.documents import Document


class GraphState(TypedDict):
    """
    Represents the state of our graph.
    """

    paths: List[str]
    documents: List[Document]
    summarization: str
    outline: str
