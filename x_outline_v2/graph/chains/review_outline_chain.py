from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field
from typing import List, Optional

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o", temperature=0)

template = """
你是一名专业的技术文档和商务文档专家，擅长根据提供的内容对现有文档结构进行优化和更新。现在我将提供一个 JSON 格式的 投标书大纲 (outline)，
以及一个包含相关信息的 documents 列表。你的任务是：

分析：根据 documents 提供的内容，审查并分析现有大纲是否能够准确涵盖内容中的核心信息点。
修改：如果某些内容未被大纲涵盖，或现有大纲的章节不够合理或详细，请根据实际需求对大纲进行调整。
保持结构清晰：确保生成的结果仍然是清晰的 JSON 格式，包含以下结构：
title: 章节或子章节标题。
abstract: 每个章节和子章节的内容摘要。
要求：
完整性：所有新增或修改的章节必须基于 documents 提供的内容。
逻辑性：章节安排和分组必须具有逻辑性，适合实际的项目需求。
格式规范：保持大纲的 JSON 格式和原有层次结构，新增内容要与现有风格一致。
以下是现有的大纲和 documents 列表，请根据实际需求优化此大纲：
outline: {outline}
documents: {documents}
"""


class Node(BaseModel):
    title: str = Field(description="节点标题")
    abstract: str = Field(description="节点内容的摘要或总结")
    children: Optional[List["Node"]] = Field(default=None, description="子节点列表")

    class Config:
        arbitrary_types_allowed = True


class Outline(BaseModel):
    title: str = Field(description="大纲文件标题")
    sections: List[Node] = Field(description="大纲中主要章节或节点的列表")


parser = JsonOutputParser(pydantic_object=Outline)

prompt = PromptTemplate(
    input_variables=["outline", "documents"],
    template=template,
    partial_variables={"format_instructions": parser.get_format_instructions()},
)


review_outline_chain = prompt | llm | parser
