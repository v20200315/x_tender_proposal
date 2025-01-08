from pydantic import BaseModel, Field
from typing import List, Optional
from langchain_core.documents import Document
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)


def length_function(documents: List[Document]) -> int:
    return sum(llm.get_num_tokens(doc.page_content) for doc in documents)


class Node(BaseModel):
    title: str = Field(description="节点标题")
    abstract: str = Field(description="节点内容的摘要或总结")
    children: Optional[List["Node"]] = Field(default=None, description="子节点列表")

    class Config:
        arbitrary_types_allowed = True


class Outline(BaseModel):
    title: str = Field(description="大纲文件标题")
    sections: List[Node] = Field(description="大纲中主要章节或节点的列表")
