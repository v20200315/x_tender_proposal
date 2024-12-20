from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

map_prompt = ChatPromptTemplate.from_messages(
    [("human", "简要概括以下内容:\\n\\n{context}")]
)

map_chain = map_prompt | llm | StrOutputParser()
