from typing import Any, Dict

from x_sandbox_2.graph.chains.generate_outline_chain import generate_outline_chain
from x_sandbox_2.graph.state import GraphState


def generate_outline(state: GraphState) -> Dict[str, Any]:
    print("---GENERATE OUTLINE (X_SANDBOX_2)---")
    summarizations = state["summarizations"]

    response = generate_outline_chain.invoke({"summarizations": summarizations})

    print(f"outline:{response.content}")

    return {"outline": response.content}
