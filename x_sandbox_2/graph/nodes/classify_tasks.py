from typing import Any, Dict

from logger_config import logger
from x_sandbox_2.graph.chains.classify_tasks_chain import classify_tasks_chain
from x_sandbox_2.graph.state import GraphState


def classify_tasks(state: GraphState) -> Dict[str, Any]:
    logger.info("---CLASSIFY TASKS (X_SANDBOX_2)---")
    structure_tasks = []
    content_tasks = []
    for task in state["tasks"]:
        response = classify_tasks_chain.invoke({"task": task})
        if response == "structure":
            structure_tasks.append(task)
        elif response == "content":
            content_tasks.append(task)
        else:
            pass

    return {"structure_tasks": structure_tasks, "content_tasks": content_tasks}
