from typing import Any, Dict

from logger_config import logger
from x_sandbox_2.graph.chains.adjust_outline_content_chain import (
    adjust_outline_content_chain,
)
from x_sandbox_2.graph.state import GraphState


def adjust_outline_content(state: GraphState) -> Dict[str, Any]:
    logger.info("---ADJUST OUTLINE CONTENT (X_SANDBOX_2)---")
    content_tasks = state["content_tasks"]
    new_outline = ""
    if content_tasks:
        for task in content_tasks:
            logger.info(f"content_tasks: {task}")
            response = adjust_outline_content_chain.invoke(
                {"task": task, "outline": state["outline"], "requirements": state["requirements"],
                 "final_summarization": state["final_summarization"]}
            )
            new_outline = response
        return {"outline": new_outline}
    else:
        return {"outline": state["outline"]}
