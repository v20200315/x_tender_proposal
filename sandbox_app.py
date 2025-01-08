from dotenv import load_dotenv

load_dotenv()

import asyncio

from logger_config import logger
from x_sandbox.graph.graph import app

if __name__ == "__main__":
    logger.info("Hello Sandbox")
    paths = [
        "/Users/victor/myfolder/workspace-ai/x_tender_proposal/temp/tender04.pdf",
    ]

    async def process():
        return await app.ainvoke(
            {"paths": paths},
            {"recursion_limit": 64},
        )

    response = asyncio.run(process())

    logger.info(response)
