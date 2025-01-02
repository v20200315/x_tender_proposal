import asyncio

from dotenv import load_dotenv

load_dotenv()

from logger_config import logger
from x_sandbox_summarization.graph.graph import app

if __name__ == "__main__":
    logger.info("Hello Sandbox SUMMARIZATION")
    paths = [
        "/Users/victor/myfolder/workspace-ai/x_tender_proposal/temp/tender05.pdf",
    ]


    async def process():
        async for step in app.astream(
                {"paths": paths},
                {"recursion_limit": 64},
        ):
            logger.info(list(step.keys()))


    asyncio.run(process())
