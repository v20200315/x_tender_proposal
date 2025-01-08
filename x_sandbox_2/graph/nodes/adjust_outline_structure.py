from typing import Any, Dict

from logger_config import logger
from x_sandbox_2.graph.chains.adjust_outline_structure_chain import (
    adjust_outline_structure_chain,
)
from x_sandbox_2.graph.state import GraphState


def adjust_outline_structure(state: GraphState) -> Dict[str, Any]:
    logger.info("---ADJUST OUTLINE STRUCTURE (X_SANDBOX_2)---")
    structure_tasks = state["structure_tasks"]
    new_outline = ""
    if structure_tasks:
        for task in structure_tasks:
            logger.info(f"structure_task: {task}")
            response = adjust_outline_structure_chain.invoke(
                {"task": task, "outline": state["outline"]}
            )
            new_outline = response
        return {"outline": new_outline}
    else:
        return {"outline": state["outline"]}
