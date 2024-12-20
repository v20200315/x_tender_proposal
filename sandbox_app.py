from dotenv import load_dotenv

load_dotenv()

from logger_config import logger
from x_sandbox.graph.graph import app

if __name__ == "__main__":
    logger.info("Hello Sandbox")
    paths = [
        "/Users/victor/myfolder/workspace-ai/x_tender_proposal/temp/tender01.pdf",
    ]
    question = "文档的结构是什么？"
    response = app.invoke(input={"paths": paths, "question": question})
    logger.info(response["generation"])
