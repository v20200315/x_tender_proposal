from typing import Any, Dict

from logger_config import logger
from x_sandbox.graph.chains.review_outline_chain import review_outline_chain
from x_sandbox.graph.state import GraphState


def review_outline(state: GraphState) -> Dict[str, Any]:
    logger.info("---REVIEW OUTLINE (X_SANDBOX)---")

    contents = state["contents"]

    new_contents = []
    for _ in range(12):
        if contents:
            new_contents.append(contents.pop(0))

    response = review_outline_chain.invoke(
        {"contents": new_contents, "outline": state["outline"]}
    )

    return {"outline": response}
