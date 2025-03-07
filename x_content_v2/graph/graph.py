from dotenv import load_dotenv

load_dotenv()

from langgraph.graph import END, StateGraph

from x_content_v2.graph.state import GraphState
from x_content_v2.graph.nodes import (
    write_draft,
    review_draft,
    write_paper,
)


def decide_to_write_paper(state):
    print("---DECIDE TO WRITE PAPER---")

    if state["todo_list"]:
        print("---DECISION: DRAFT---")
        return "write_draft"
    else:
        print("---DECISION: PAPER---")
        return "write_paper"


workflow = StateGraph(GraphState)

workflow.add_node("write_draft", write_draft)
workflow.add_node("review_draft", review_draft)
workflow.add_node("write_paper", write_paper)

workflow.set_entry_point("write_draft")
workflow.add_edge("write_draft", "review_draft")
workflow.add_conditional_edges(
    "review_draft",
    decide_to_write_paper,
    {
        "write_draft": "write_draft",
        "write_paper": "write_paper",
    },
)

workflow.add_edge("write_paper", END)


app = workflow.compile()

app.get_graph().draw_mermaid_png(output_file_path="x_content_v2/graph.png")
