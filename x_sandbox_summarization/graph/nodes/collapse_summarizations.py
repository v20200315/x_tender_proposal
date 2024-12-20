from typing import Any, Dict, List

from langchain.chains.combine_documents import split_list_of_docs, acollapse_docs
from langchain_core.documents import Document
from langchain_openai import ChatOpenAI

from x_sandbox_summarization.graph.chains.reduce_chain import reduce_chain
from x_sandbox_summarization.graph.state import GraphState

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

token_max = 3000


def length_function(documents: List[Document]) -> int:
    return sum(llm.get_num_tokens(doc.page_content) for doc in documents)


async def collapse_summarizations(state: GraphState) -> Dict[str, Any]:
    doc_lists = split_list_of_docs(
        state["collapsed_summarizations"], length_function, token_max
    )
    results = []
    for doc_list in doc_lists:
        results.append(await acollapse_docs(doc_list, reduce_chain.ainvoke))

    return {"collapsed_summarizations": results}
