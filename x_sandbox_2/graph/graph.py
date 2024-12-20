from dotenv import load_dotenv

load_dotenv()

from langgraph.graph import END, StateGraph

from x_sandbox_2.graph.state import GraphState
from x_sandbox_2.graph.nodes import load_docs, summarize_docs


workflow = StateGraph(GraphState)

workflow.add_node("load_docs", load_docs)
workflow.add_node("summarize_docs", summarize_docs)

workflow.set_entry_point("load_docs")
workflow.add_edge("load_docs", "summarize_docs")
workflow.add_edge("summarize_docs", END)


app = workflow.compile()

app.get_graph().draw_mermaid_png(output_file_path="x_sandbox_2/graph.png")
