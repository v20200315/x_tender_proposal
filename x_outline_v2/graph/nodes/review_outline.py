from typing import Any, Dict

from logger_config import logger
from x_outline_v2.graph.chains.review_outline_chain import review_outline_chain
from x_outline_v2.graph.state import GraphState


def review_outline(state: GraphState) -> Dict[str, Any]:
    logger.info("---REVIEW OUTLINE (X_OUTLINE_V2)---")
    documents = state["documents"]
    outline = state["outline"]

    new_documents = []
    for _ in range(3):
        if documents:
            new_documents.append(documents.pop(0))

    logger.info(len(documents))
    response = review_outline_chain.invoke(
        {"documents": new_documents, "outline": outline}
    )

    return {"outline": response}
