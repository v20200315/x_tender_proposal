from dotenv import load_dotenv

load_dotenv()

from langgraph.graph import END, StateGraph

from x_sandbox.graph.state import GraphState
from x_sandbox.graph.nodes import (
    load_docs,
    summarize_docs,
    generate_outline,
)


workflow = StateGraph(GraphState)

workflow.add_node("load_docs", load_docs)
workflow.add_node("summarize_docs", summarize_docs)
workflow.add_node("generate_outline", generate_outline)

workflow.set_entry_point("load_docs")
workflow.add_edge("load_docs", "summarize_docs")
workflow.add_edge("summarize_docs", "generate_outline")
workflow.add_edge("generate_outline", END)


app = workflow.compile()

app.get_graph().draw_mermaid_png(output_file_path="x_sandbox/graph.png")
