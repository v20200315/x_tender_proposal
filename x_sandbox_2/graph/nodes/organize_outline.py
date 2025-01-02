from typing import Any, Dict

from logger_config import logger
from x_sandbox_2.graph.state import GraphState


def organize_outline(state: GraphState) -> Dict[str, Any]:
    logger.info("---ORGANIZE OUTLINE (X_SANDBOX_2)---")
    logger.info(state["outline"])

    return {"organized_outline": state["outline"]}
