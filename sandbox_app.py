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
        async for step in app.astream(
                {"paths": paths},
                {"outline": "this is outline"},
                {"recursion_limit": 64},
        ):
            logger.info(list(step.keys()))


    asyncio.run(process())
