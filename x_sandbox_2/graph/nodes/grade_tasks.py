from typing import Any, Dict

from logger_config import logger
from x_sandbox_2.graph.chains.grade_tasks_chain import grade_tasks_chain
from x_sandbox_2.graph.state import GraphState


def grade_tasks(state: GraphState) -> Dict[str, Any]:
    logger.info("---GRADE TASKS (X_SANDBOX_2)---")
    filtered_tasks = []
    for task in state["tasks"]:
        response = grade_tasks_chain.invoke({"task": task})
        if response == "yes":
            filtered_tasks.append(task)

    logger.info(filtered_tasks)

    return {"tasks": filtered_tasks}
