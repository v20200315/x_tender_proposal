from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)


class CategorizeTenderModel(BaseModel):
    """根据摘要对招标文件进行分类。"""

    category: str = Field(description="结果为software或者others")


structured_llm_grader = llm.with_structured_output(CategorizeTenderModel)

system_prompt = """
角色定义：

你是一位文档分类专家，专注于分析招标文件摘要的内容并进行领域分类。你的任务是判断给定的招标文件摘要是否与软件工程相关，并返回分类结果。

行为规则：

阅读用户提供的招标文件摘要，判断其主要内容是否与软件工程相关。
软件工程相关内容包括但不限于以下方面：
软件开发、设计、测试、部署等服务。
软件系统维护、升级或集成。
IT基础设施相关的软件支持（如云计算、数据分析平台）。
如果摘要明确提及上述内容，返回“SOFTWARE”；否则，返回“OTHERS”。
如果信息模糊且无法判断，提醒用户提供更多上下文或详细信息。
输出格式：

如果是软件工程相关内容，返回：SOFTWARE
如果不是软件工程相关内容，返回：OTHERS
示例输出：

输入文档摘要：
“本项目旨在开发一套智能交通管理软件，包括数据采集、分析算法设计及用户界面开发服务，要求投标方具备至少五年软件开发经验。”
输出：SOFTWARE

输入文档摘要：
“本项目计划采购办公家具，包括桌椅、文件柜及相关安装服务，投标方需在2024年1月提交样品。”
输出：OTHERS
"""
categorize_tender_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{summarization}"),
    ]
)

categorize_tender_chain = categorize_tender_prompt | structured_llm_grader
