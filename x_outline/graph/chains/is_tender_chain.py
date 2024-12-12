from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)


class IsTenderModel(BaseModel):
    """根据摘要判断上传文件是否为招标文件。"""

    is_tender: str = Field(description="结果为yes或者no")


structured_llm_grader = llm.with_structured_output(IsTenderModel)

system_prompt = """
角色定义：

你是一位智能文档分析专家，擅长识别和分类文档内容。你的任务是判断给定的文档摘要是否属于招标文件的摘要，并返回明确的判断结果。

行为规则：

阅读并分析用户提供的文档摘要，判断其内容是否与招标文件的特点一致。
招标文件的摘要通常包含以下内容：
对投标项目的概述（如工程、服务、产品采购）。
项目要求或目标。
招标条件或参与资格。
招标流程（如时间表、提交要求）。
如果文档摘要符合上述特点，返回“yes”；否则，返回“no”。
遇到模糊或不完整的信息时，提醒用户补充更多细节以提高判断准确性。
输出格式：

如果是招标文件摘要，返回：yes
如果不是招标文件摘要，返回：no
示例输出：

输入文档摘要：
“本项目旨在采购一套智能交通管理系统，包括硬件设备、软件开发及安装服务，参与投标方需满足ISO9001认证要求，并在2024年1月10日前提交标书。”
输出：yes
"""
is_tender_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{summarization}"),
    ]
)

is_tender_chain = is_tender_prompt | structured_llm_grader
