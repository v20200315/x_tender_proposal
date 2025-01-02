from dotenv import load_dotenv

load_dotenv()

import asyncio

from logger_config import logger
from x_sandbox_2.graph.graph import app

if __name__ == "__main__":
    logger.info("Hello Sandbox 2")


    async def process():
        async for step in app.astream(
                {"outline": "this is outline"},
                {"recursion_limit": 64},
        ):
            logger.info(step)


    asyncio.run(process())
