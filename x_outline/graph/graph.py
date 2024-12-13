from dotenv import load_dotenv

load_dotenv()

from langgraph.graph import END, StateGraph

from x_outline.graph.state import GraphState
from x_outline.graph.nodes import (
    load_docs,
    summarize_docs,
    is_tender,
    categorize_tender,
    generate_outline,
)


def decide_to_category(state):
    print("---ASSESS TENDER STATE---")
    if state["tender"] == "yes":
        return "categorize_tender"
    else:
        return END


workflow = StateGraph(GraphState)

workflow.add_node("load_docs", load_docs)
# workflow.add_node("summarize_docs", summarize_docs)
# workflow.add_node("is_tender", is_tender)
# workflow.add_node("categorize_tender", categorize_tender)
workflow.add_node("generate_outline", generate_outline)

# workflow.set_entry_point("load_docs")
# workflow.add_edge("load_docs", "summarize_docs")
# workflow.add_edge("summarize_docs", "is_tender")
# workflow.add_conditional_edges(
#     "is_tender",
#     decide_to_category,
#     {
#         "categorize_tender": "categorize_tender",
#         END: END,
#     },
# )
#
# workflow.add_edge("categorize_tender", "generate_outline")
# workflow.add_edge("generate_outline", END)

workflow.set_entry_point("load_docs")
workflow.add_edge("load_docs", "generate_outline")
workflow.add_edge("generate_outline", END)

app = workflow.compile()

app.get_graph().draw_mermaid_png(output_file_path="x_outline/graph.png")
