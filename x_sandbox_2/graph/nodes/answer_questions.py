from typing import Any, Dict

from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

from x_sandbox_2.graph.chains.answer_questions_chain import answer_questions_chain
from x_sandbox_2.graph.state import GraphState


def answer_questions(state: GraphState) -> Dict[str, Any]:
    print("---ANSWER QUESTIONS (X_SANDBOX_2)---")
    questions = [
        "项目的名称是什么",
        "客户的主要需求是什么？客户的核心目标是什么？例如，提高效率、节省成本、增强功能等。",
        "客户为何发起这个项目？这个项目是否有特定的原因，如解决现有系统的问题、拓展业务或满足法规要求",
        "该项目的背景信息有哪些？是否有之前的项目或研究背景，可以帮助理解本次需求的脉络？",
        "有哪些技术或平台要求？例如，是否要求特定的技术栈、操作系统、数据库、编程语言等？",
        "招标书中列出的功能需求是否清晰？是否有重点和优先级？",
        "是否有特定的安全规范或合规性要求？例如，数据加密、用户认证等。",
        "是否有明确的时间表、里程碑、阶段性目标？",
        "客户是否设定了具体的启动和完成日期？是否存在必须遵守的时间节点？",
        "是否有明确的预算限制？预算的分配和优先级如何？",
    ]

    retriever = Chroma(
        collection_name="rag-chroma",
        persist_directory="./.chroma",
        embedding_function=OpenAIEmbeddings(),
    ).as_retriever()

    qas = []

    for question in questions:
        documents = retriever.invoke(question)
        answer = answer_questions_chain.invoke(
            {"context": documents, "question": question}
        )
        print(f"Q: {question}")
        print(f"A: {answer}")
        qas.append(answer)
    return {"qas": qas}
