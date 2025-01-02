from typing import TypedDict, Annotated, List
from langchain_core.documents import Document
import operator


class GraphState(TypedDict):
    """
    Represents the state of our graph.
    """

    paths: List[str]
    contents: List[str]
    content: str
    summarizations: Annotated[list, operator.add]
    collapsed_summarizations: List[Document]
    final_summarization: str
    classification: str
    search_results: str
    outline: str
    organized_outline: str
