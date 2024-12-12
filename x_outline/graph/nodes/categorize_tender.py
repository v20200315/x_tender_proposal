from typing import Any, Dict

from x_outline.graph.chains.categorize_tender_chain import categorize_tender_chain
from x_outline.graph.state import GraphState


def categorize_tender(state: GraphState) -> Dict[str, Any]:

    print("---CATEGORIZE TENDER---")
    summarization = state["summarization"]

    result = categorize_tender_chain.invoke({"summarization": summarization}).category

    if result.lower() == "software":
        print("---CATEGORIZE TENDER: SOFTWARE---")
    else:
        print("---CATEGORIZE TENDER: OTHER---")

    return {"tender_category": result.lower()}
