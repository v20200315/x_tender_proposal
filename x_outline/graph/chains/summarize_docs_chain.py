from langchain.chains.summarize import load_summarize_chain
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.llms import Tongyi

prompt = PromptTemplate.from_template(
    """
    请为以下内容撰写一份简明扼要的摘要：

    「{text}」

    注意：摘要应准确概括主要信息，避免冗长，且不要遗漏关键点。

    简明摘要：
    """
)


def get_summarize_docs_chain(llm_type):
    if llm_type == "通义千问":
        llm = Tongyi(model="qwen-plus", temperature=0)
    else:
        llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    summarize_docs_chain = load_summarize_chain(
        llm,
        chain_type="stuff",
        prompt=prompt,
    )

    return summarize_docs_chain
