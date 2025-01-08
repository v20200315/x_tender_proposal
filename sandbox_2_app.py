from dotenv import load_dotenv

load_dotenv()

from logger_config import logger
from x_sandbox_2.graph.graph import app

if __name__ == "__main__":
    logger.info("Hello Sandbox 2")

    app.invoke(
        input={
            "feedback": "去掉第三章第一小节，并把第二章增加小节小节的名称是需求分析，然后根据评分因素及评审标准优化outline，并着重根据评分完成outline的优化",
        }
    )
