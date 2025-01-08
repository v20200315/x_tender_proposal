from dotenv import load_dotenv

load_dotenv()

from langgraph.constants import START, END
from langgraph.graph import StateGraph

from x_sandbox_3.graph.state import GraphState
from x_sandbox_3.graph.nodes import (
    load_docs,
    generate_keywords,
)

workflow = StateGraph(GraphState)

workflow.add_node("load_docs", load_docs)
workflow.add_node("generate_keywords", generate_keywords)

workflow.add_edge(START, "load_docs")
workflow.add_edge("load_docs", "generate_keywords")
workflow.add_edge("generate_keywords", END)

app = workflow.compile()

app.get_graph().draw_mermaid_png(output_file_path="x_sandbox_3/graph.png")
