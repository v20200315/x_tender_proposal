from typing import Any, Dict

from x_sandbox.graph.chains.summarize_docs_chain import summarize_docs_chain
from x_sandbox.graph.state import GraphState


def summarize_docs(state: GraphState) -> Dict[str, Any]:
    print("---SUMMARIZE DOCS (X_SANDBOX)---")
    documents = state["documents"]

    summarization = summarize_docs_chain.invoke({"documents": documents})

    # print("summarize_docs:")
    # print(summarization)
    print("=" * 20)
    print(summarization.content)
    print("=" * 20)

    return {"summarization": summarization.content}
