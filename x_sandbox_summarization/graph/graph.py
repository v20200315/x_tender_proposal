from typing import List, Literal

from dotenv import load_dotenv

load_dotenv()

from langgraph.constants import Send, START
from langgraph.graph import END, StateGraph
from langchain_core.documents import Document
from langchain_openai import ChatOpenAI

from x_sandbox_summarization.graph.state import GraphState
from x_sandbox_summarization.graph.nodes import load_docs, generate_summarization, collect_summarizations, \
    collapse_summarizations, generate_final_summarization


def map_summarizations(state: GraphState):
    return [
        Send("generate_summarization", {"content": content}) for content in state["contents"]
    ]


llm = ChatOpenAI(model="gpt-4o", temperature=0)

token_max = 3000


def length_function(documents: List[Document]) -> int:
    return sum(llm.get_num_tokens(doc.page_content) for doc in documents)


def should_collapse(
        state: GraphState,
) -> Literal["collapse_summarizations", "generate_final_summarization"]:
    num_tokens = length_function(state["collapsed_summarizations"])
    if num_tokens > token_max:
        return "collapse_summarizations"
    else:
        return "generate_final_summarization"


workflow = StateGraph(GraphState)

workflow.add_node("load_docs", load_docs)
workflow.add_node("generate_summarization", generate_summarization)
workflow.add_node("collect_summarizations", collect_summarizations)
workflow.add_node("collapse_summarizations", collapse_summarizations)
workflow.add_node("generate_final_summarization", generate_final_summarization)

workflow.add_edge(START, "load_docs")
workflow.add_conditional_edges("load_docs", map_summarizations, ["generate_summarization"])
workflow.add_edge("generate_summarization", "collect_summarizations")
workflow.add_conditional_edges("collect_summarizations", should_collapse)
workflow.add_conditional_edges("collapse_summarizations", should_collapse)
workflow.add_edge("generate_final_summarization", END)

app = workflow.compile()

app.get_graph().draw_mermaid_png(output_file_path="x_sandbox_summarization/graph.png")
