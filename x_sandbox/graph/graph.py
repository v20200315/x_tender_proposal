from dotenv import load_dotenv

load_dotenv()

from typing import Literal

from langgraph.constants import Send, START, END
from langgraph.graph import StateGraph

from logger_config import logger
from x_sandbox.graph.consts import TOKEN_MAX
from x_sandbox.graph.tools import length_function

from x_sandbox.graph.state import GraphState
from x_sandbox.graph.nodes import (
    load_docs,
    generate_summarization,
    collect_summarizations,
    collapse_summarizations,
    generate_final_summarization,
    classify_summarization,
    generate_outline,
    review_outline,
    organize_outline,
)


def map_summarizations(state: GraphState):
    return [
        Send("generate_summarization", {"content": content}) for content in state["contents"]
    ]


def should_collapse(state: GraphState) -> Literal["collapse_summarizations", "generate_final_summarization"]:
    num_tokens = length_function(state["collapsed_summarizations"])
    logger.info("---SHOULD COLLAPSE---")
    if num_tokens > TOKEN_MAX:
        logger.info("---DECISION: COLLAPSE---")
        return "collapse_summarizations"
    else:
        logger.info("---DECISION: GENERATE---")
        return "generate_final_summarization"


def decide_to_end(state: GraphState) -> Literal["review_outline", "organize_outline"]:
    logger.info("---DECIDE TO END---")

    if state["contents"]:
        print("---DECISION: REVIEW---")
        return "review_outline"
    else:
        print("---DECISION: ORGANIZE---")
        return "organize_outline"


workflow = StateGraph(GraphState)

workflow.add_node("load_docs", load_docs)
workflow.add_node("generate_summarization", generate_summarization)
workflow.add_node("collect_summarizations", collect_summarizations)
workflow.add_node("collapse_summarizations", collapse_summarizations)
workflow.add_node("generate_final_summarization", generate_final_summarization)
workflow.add_node("classify_summarization", classify_summarization)
workflow.add_node("generate_outline", generate_outline)
workflow.add_node("review_outline", review_outline)
workflow.add_node("organize_outline", organize_outline)

workflow.add_edge(START, "load_docs")
workflow.add_conditional_edges("load_docs", map_summarizations, ["generate_summarization"])
workflow.add_edge("generate_summarization", "collect_summarizations")
workflow.add_conditional_edges("collect_summarizations", should_collapse)
workflow.add_conditional_edges("collapse_summarizations", should_collapse)
workflow.add_edge("generate_final_summarization", "classify_summarization")
workflow.add_edge("classify_summarization", "generate_outline")
workflow.add_edge("generate_outline", "review_outline")
workflow.add_conditional_edges("review_outline", decide_to_end)
workflow.add_edge("organize_outline", END)

app = workflow.compile()

app.get_graph().draw_mermaid_png(output_file_path="x_sandbox/graph.png")
