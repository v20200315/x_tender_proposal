from typing import Any, Dict

from x_outline.graph.chains.summarize_docs_chain import summarize_docs_chain
from x_outline.graph.state import GraphState


def summarize_docs(state: GraphState) -> Dict[str, Any]:
    print("---SUMMARIZE DOCS---")
    documents = state["documents"]

    summarization = summarize_docs_chain.invoke({"documents": documents})

    # print("summarize_docs:")
    # print(summarization)
    # print("=" * 20)
    # print(summarization.content)
    # print("=" * 20)

    return {"summarization": summarization.content}
