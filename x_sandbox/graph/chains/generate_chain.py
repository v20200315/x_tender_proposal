from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o", temperature=0)
prompt = hub.pull("rlm/rag-prompt")

generate_chain = prompt | llm | StrOutputParser()
