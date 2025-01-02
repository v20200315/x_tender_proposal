from typing import Any, Dict

from logger_config import logger
from x_sandbox.graph.state import GraphState


def organize_outline(state: GraphState) -> Dict[str, Any]:
    logger.info("---ORGANIZE OUTLINE (X_SANDBOX)---")
    logger.info(state["outline"])

    return {"organized_outline": state["outline"]}
