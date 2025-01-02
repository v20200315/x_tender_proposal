from dotenv import load_dotenv

load_dotenv()

from langgraph.constants import START, END
from langgraph.graph import StateGraph

from x_sandbox_2.graph.state import GraphState
from x_sandbox_2.graph.nodes import (
    organize_outline,
)

workflow = StateGraph(GraphState)

workflow.add_node("organize_outline", organize_outline)

workflow.add_edge(START, "organize_outline")
workflow.add_edge("organize_outline", END)

app = workflow.compile()

app.get_graph().draw_mermaid_png(output_file_path="x_sandbox_2/graph.png")
