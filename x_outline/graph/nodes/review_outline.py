from typing import Any, Dict

from logger_config import logger
from x_outline_v2.graph.state import GraphState


def review_outline(state: GraphState) -> Dict[str, Any]:
    logger.info("---REVIEW OUTLINE(NO USE) (X_OUTLINE)---")
    documents = state["documents"]
    outline = state["outline"]

    new_documents = []
    for _ in range(5):
        if documents:
            new_documents.append(documents.pop(0))

    logger.info(len(documents))

    return {"outline": outline}
