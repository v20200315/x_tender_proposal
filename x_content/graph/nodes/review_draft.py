from typing import Any, Dict

from logger_config import logger
from x_content_v2.graph.state import GraphState


def review_draft(state: GraphState) -> Dict[str, Any]:
    logger.info("---REVIEW DRAFT(NO USE) (X_CONTENT)---")
    doing = state["doing"]
    done_list = state["done_list"]

    done_list.append(doing)

    return {"done_list": done_list}
