from dotenv import load_dotenv

load_dotenv()

from langgraph.graph import START, END, StateGraph

from x_sandbox.graph.state import GraphState
from x_sandbox.graph.nodes import (
    load_docs,
    retrieve,
    generate,
)


workflow = StateGraph(GraphState)

workflow.add_node("load_docs", load_docs)
workflow.add_node("retrieve", retrieve)
workflow.add_node("generate", generate)

workflow.add_edge(START, "load_docs")
workflow.add_edge("load_docs", "retrieve")
workflow.add_edge("retrieve", "generate")
workflow.add_edge("generate", END)


app = workflow.compile()

app.get_graph().draw_mermaid_png(output_file_path="x_sandbox/graph.png")
