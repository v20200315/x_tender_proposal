from typing import Any, Dict

from logger_config import logger
from x_content_v2.graph.chains.review_draft_chain import review_draft_chain
from x_content_v2.graph.state import GraphState


def review_draft(state: GraphState) -> Dict[str, Any]:
    logger.info("---REVIEW DRAFT (X_CONTENT_V2)---")
    doing = state["doing"]
    done_list = state["done_list"]

    response = review_draft_chain.invoke({"content": doing["content"]})
    doing["content"] = response.content
    done_list.append(doing)

    return {"done_list": done_list}
