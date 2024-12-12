from typing import Any, Dict
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

from x_section.graph.state import GraphState


def load_docs(state: GraphState) -> Dict[str, Any]:
    print("---LOAD DOCS (X_SECTION)---")
    paths = state["paths"]

    docs = [PyPDFLoader(path).load() for path in paths]
    docs_list = [item for sublist in docs for item in sublist]

    # 文本分割
    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=1000, chunk_overlap=100
    )
    documents = text_splitter.split_documents(docs_list)

    return {"documents": documents}
