from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o", temperature=0)

system_prompt = """

"""

generate_questions_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        (
            "human",
            "{summarization}",
        ),
    ]
)

generate_questions_chain = generate_questions_prompt | llm
