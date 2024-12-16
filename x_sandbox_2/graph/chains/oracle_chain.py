from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field
from typing import List, Optional

from langchain_core.prompts import (
    PromptTemplate,
    ChatPromptTemplate,
    MessagesPlaceholder,
)
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

system_prompt = """
    """

# 为对话流创建提示模板。
prompt = ChatPromptTemplate.from_messages(
    [
        # AI的角色和规则。
        ("system", system_prompt),
        # 过去的聊天消息以维持上下文。
        MessagesPlaceholder(variable_name="chat_history"),
        # 用户的输入。
        ("user", "{input}"),
        # 助手的便笺簿，以跟踪工具使用情况和中间步骤。
        ("assistant", "scratchpad: {scratchpad}"),
    ]
)

oracle_chain = prompt | llm
