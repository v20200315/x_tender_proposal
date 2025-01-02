from typing import Any, Dict

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from x_sandbox_summarization.graph.state import GraphState


def load_docs(state: GraphState) -> Dict[str, Any]:
    print("---LOAD DOCS (X_SANDBOX_SUMMARIZATION)---")
    paths = state["paths"]

    docs = [PyPDFLoader(path).load() for path in paths]
    docs_list = [item for sublist in docs for item in sublist]

    # 文本分割
    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=3000, chunk_overlap=200
    )
    split_docs = text_splitter.split_documents(docs_list)
    contents = [doc.page_content for doc in split_docs]

    return {"contents": contents}
