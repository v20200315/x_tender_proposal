from typing import List, TypedDict

from pydantic import Json


class GraphState(TypedDict):
    """
    Represents the state of our graph.
    """

    project_name: str
    outline: str
    todo_list: List[Json]
    doing: Json
    done_list: List[Json]
    summarizations: List[str]
    images: bool
    min_length: int
    article_path: str
