from typing import Any, Dict

from x_outline.graph.chains.is_tender_chain import is_tender_chain
from x_outline.graph.state import GraphState


def is_tender(state: GraphState) -> Dict[str, Any]:

    print("---IS TENDER---")
    summarization = state["summarization"]

    result = is_tender_chain.invoke({"summarization": summarization}).is_tender

    if result.lower() == "yes":
        print("---IS TENDER: YES---")
    else:
        print("---IS TENDER: NO---")

    return {"tender": result.lower()}
