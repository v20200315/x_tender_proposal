from dotenv import load_dotenv

load_dotenv()
from logger_config import logger
from x_sandbox_2.graph.graph import app


if __name__ == "__main__":
    logger.info("Hello Sandbox 2")
    paths = [
        "/Users/victor/myfolder/workspace-ai/x_tender_proposal/temp/tender01.pdf",
    ]
    response = app.invoke(input={"paths": paths})
