import asyncio
from time import sleep

from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader

from logger_config import logger

if __name__ == "__main__":
    file_path = "/Users/victor/myfolder/workspace-ai/x_tender_proposal/temp/tender04.pdf"
    pages = PyPDFLoader(file_path).load()
    contents = []
    for page in pages:
        contents.append(page.page_content)
    content = "".join(contents[10:23])
    logger.info(content)

    # file_path = "/Users/victor/myfolder/workspace-ai/x_tender_proposal/temp/tender0501.docx"
    # pages = Docx2txtLoader(file_path).load()
    # logger.info(len(pages))

    # file_path = "/Users/victor/myfolder/workspace-ai/x_tender_proposal/temp/tender0502.docx"
    # data = Docx2txtLoader(file_path).load()
    # document = data[0]
    # content = "".join(document.page_content.splitlines())
    # logger.info(content)
