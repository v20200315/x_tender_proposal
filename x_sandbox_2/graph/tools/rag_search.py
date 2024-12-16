from typing import List

from langchain_core.documents import Document
from langchain_core.tools import tool
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings


@tool("rag_search")
def rag_search(query: str) -> List[Document]:
    retriever = Chroma(
        collection_name="rag-chroma",
        persist_directory="./.chroma",
        embedding_function=OpenAIEmbeddings(),
    ).as_retriever()

    documents = retriever.invoke(query)

    return documents
