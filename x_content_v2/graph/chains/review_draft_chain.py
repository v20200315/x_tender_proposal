from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o", temperature=0)

template = """
你是一位专业的写作编辑。以下是文章的一部分，请对其进行以下操作：
1. 检查语法和拼写错误。
2. 修改句子以提高清晰度和流畅性，同时保持原意。
3. 如果有冗长或重复的内容，进行精简。

以下是需要编辑的文本：
{content}

请输出修改后的文本。
"""

prompt = PromptTemplate(input_variables=["content"], template=template)


review_draft_chain = prompt | llm
