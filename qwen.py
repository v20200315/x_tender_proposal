from dotenv import load_dotenv
from langchain.chains.llm import LLMChain

load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import Tongyi

llm = Tongyi(model="qwen-plus", temperature=1)
template = """
        你的名字是小黑子,当人问问题的时候,你都会在开头加上'唱,跳,rap,篮球!',然后再回答{question}
    """
prompt = PromptTemplate(
    template=template,
    input_variables=["question"],  # 这个question就是用户输入的内容,这行代码不可缺少
)
chain = prompt | llm
question = "你现在使用的大预言模型的名称是什么，是qwen-plus还是其他的"

res = chain.invoke(question)  # 运行

print(res)  # 打印结果
