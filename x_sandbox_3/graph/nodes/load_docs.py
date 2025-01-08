import copy
from typing import Any, Dict

from langchain_community.document_loaders import PyPDFLoader

from logger_config import logger
from x_sandbox_3.graph.state import GraphState


def load_docs(state: GraphState) -> Dict[str, Any]:
    logger.info("---LOAD DOCS (X_SANDBOX_3)---")
    paths = state["paths"]

    docs = [PyPDFLoader(path).load() for path in paths]
    contents = [page for doc in docs for page in doc]
    copied_contents = copy.deepcopy(contents)

    return {"contents": contents, "copied_contents": copied_contents}


# # 文本分割
# text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
#     model_name="gpt-4", chunk_size=3000, chunk_overlap=300
# )
# doc_splits = text_splitter.split_documents(pages)
#
# client_settings = chromadb.config.Settings(
#     is_persistent=True,
#     persist_directory='my_dir',
#     anonymized_telemetry=False,
# )
#
# vector = Chroma(
#     collection_name='my_collection',
#     client_settings=client_settings,
#     embedding_function=OpenAIEmbeddings(),
# )
#
# vector.add_documents(doc_splits)
