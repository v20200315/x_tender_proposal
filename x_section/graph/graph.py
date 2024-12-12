from dotenv import load_dotenv

load_dotenv()

from langgraph.graph import END, StateGraph

from x_section.graph.state import GraphState
from x_section.graph.nodes import (
    load_docs,
    generate_query,
    write_draft,
)


workflow = StateGraph(GraphState)

workflow.add_node("load_docs", load_docs)
workflow.add_node("generate_query", generate_query)
workflow.add_node("write_draft", write_draft)

workflow.set_entry_point("load_docs")


workflow.add_edge("load_docs", "generate_query")
workflow.add_edge("generate_query", "write_draft")
workflow.add_edge("write_draft", END)


app = workflow.compile()

app.get_graph().draw_mermaid_png(output_file_path="x_section/graph.png")
