from typing import TypedDict, List
from langchain_core.documents import Document


class GraphState(TypedDict):
    """
    Represents the state of our graph.
    """

    paths: List[str]
    contents: List[Document]
    copied_contents: List[Document]
    final_summarization: str
    classification: str
    keywords: List[str]
