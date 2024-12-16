from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
prompt = hub.pull("rlm/rag-prompt")

answer_questions_chain = prompt | llm | StrOutputParser()
