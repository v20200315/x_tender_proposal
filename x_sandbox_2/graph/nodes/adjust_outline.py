from typing import Any, Dict

from logger_config import logger
from x_sandbox_2.graph.chains.adjust_outline_chain import adjust_outline_chain
from x_sandbox_2.graph.state import GraphState


def adjust_outline(state: GraphState) -> Dict[str, Any]:
    logger.info("---ADJUST OUTLINE (X_SANDBOX_2)---")
    structure_tasks = state["structure_tasks"]
    content_tasks = state["content_tasks"]
    response = adjust_outline_chain.invoke(
        {
            "structure_tasks": structure_tasks,
            "content_tasks": content_tasks,
            "outline": state["outline"],
            "requirements": state["requirements"],
            "final_summarization": state["final_summarization"]
        }
    )
    """
    输入参数是调整大纲结构的任务集(structure_tasks),调整大纲内容的任务集(content_tasks),初始的大纲(outline),大纲对应需求集合(requirements)以及大纲对应文档的摘要(final_summarization).
    任务是以大纲对应需求集合(requirements)和大纲对应文档的摘要(final_summarization)作为参考,完成调整大纲结构的任务集(structure_tasks)和调整大纲内容的任务集(content_tasks)，这些所有的任务都是对初始的大纲(outline)调整优化的建议.
    """
    return {"outline": response}
