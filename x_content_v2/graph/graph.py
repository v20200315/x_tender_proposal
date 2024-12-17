from dotenv import load_dotenv

load_dotenv()

from langgraph.graph import END, StateGraph

from x_content_v2.graph.state import GraphState
from x_content_v2.graph.nodes import (
    write_draft,
)


workflow = StateGraph(GraphState)

workflow.add_node("write_draft", write_draft)

workflow.set_entry_point("write_draft")


workflow.add_edge("write_draft", END)


app = workflow.compile()

app.get_graph().draw_mermaid_png(output_file_path="x_content_v2/graph.png")
