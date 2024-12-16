from typing import Any, Dict

from x_sandbox_2.graph.chains.summarize_docs_chain2 import summarize_docs_chain
from x_sandbox_2.graph.state import GraphState


def summarize_docs(state: GraphState) -> Dict[str, Any]:
    print("---SUMMARIZE DOCS (X_SANDBOX_2)---")
    documents = state["documents"]

    # response = summarize_docs_chain.invoke({"documents": documents})
    summarizations = []
    for i in range(0, len(documents), 3):
        chunk = documents[i : i + 3]
        response = summarize_docs_chain.invoke(chunk)
        print(f"summarization: {response["output_text"]}")
        summarizations.append(response["output_text"])

    return {"summarizations": summarizations}
