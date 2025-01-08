from dotenv import load_dotenv

load_dotenv()

from typing import Literal

from langgraph.constants import START, END
from langgraph.graph import StateGraph

from logger_config import logger
from x_sandbox_2.graph.state import GraphState
from x_sandbox_2.graph.nodes import (
    parse_feedback,
    grade_tasks,
    classify_tasks,
    adjust_outline,
)


def decide_to_end_or_classify_tasks(state: GraphState):
    logger.info("---DECIDE TO END OR CLASSIFY TASKS---")

    if state["tasks"]:
        logger.info("---DECISION: CLASSIFY---")
        return "classify_tasks"
    else:
        logger.info("---DECISION: END---")
        return END


workflow = StateGraph(GraphState)

workflow.add_node("parse_feedback", parse_feedback)
workflow.add_node("grade_tasks", grade_tasks)
workflow.add_node("classify_tasks", classify_tasks)
workflow.add_node("adjust_outline", adjust_outline)

workflow.add_edge(START, "parse_feedback")
workflow.add_edge("parse_feedback", "grade_tasks")
workflow.add_conditional_edges(
    "grade_tasks",
    decide_to_end_or_classify_tasks,
    {
        "classify_tasks": "classify_tasks",
        END: END,
    },
)
workflow.add_edge("classify_tasks", "adjust_outline")
workflow.add_edge("adjust_outline", END)

app = workflow.compile()

app.get_graph().draw_mermaid_png(output_file_path="x_sandbox_2/graph.png")
