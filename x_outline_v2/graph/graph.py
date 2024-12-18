from dotenv import load_dotenv

load_dotenv()

from langgraph.graph import END, StateGraph

from x_outline_v2.graph.state import GraphState
from x_outline_v2.graph.nodes import (
    load_docs,
    summarize_docs,
    generate_outline,
    review_outline,
)

print()


def decide_to_end(state):
    print("---DECIDE TO END---")

    if state["documents"]:
        print("---DECISION: REVIEW---")
        return "review_outline"
    else:
        print("---DECISION: END---")
        return END


workflow = StateGraph(GraphState)

workflow.add_node("load_docs", load_docs)
workflow.add_node("summarize_docs", summarize_docs)
workflow.add_node("generate_outline", generate_outline)
workflow.add_node("review_outline", review_outline)

workflow.set_entry_point("load_docs")
workflow.add_edge("load_docs", "summarize_docs")
workflow.add_edge("summarize_docs", "generate_outline")
workflow.add_edge("generate_outline", "review_outline")

# workflow.add_node("load_docs", load_docs)
# workflow.add_node("review_outline", review_outline)
#
# workflow.set_entry_point("load_docs")
# workflow.add_edge("load_docs", "review_outline")

workflow.add_conditional_edges(
    "review_outline",
    decide_to_end,
    {
        "review_outline": "review_outline",
        END: END,
    },
)


app = workflow.compile()

app.get_graph().draw_mermaid_png(output_file_path="x_outline_v2/graph.png")
