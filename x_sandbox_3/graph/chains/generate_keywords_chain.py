from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, ListOutputParser
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

generate_keywords_template = """
你是一位专业的投标需求分析专家，擅长根据投标分类和文档摘要提取相关需求关键词。以下是用户提供的信息：  

\\n\\n投标分类 (classification)：{classification}  
文档摘要 (final_summarization)：{final_summarization}  

\\n\\n请根据以下要求生成需求关键词：  

1. 阅读文档摘要 (final_summarization)，提取其中与需求相关的关键信息。  
2. 根据提供的分类 (classification)，结合文档摘要中的内容，分析通常涉及的服务或产品需求。  
3. 提取50个精准的关键词，确保关键词涵盖分类领域下的核心需求并与文档摘要内容匹配。  
4. 输出关键词列表，每个关键词单独占一行，列表总数为50个，不多不少。  

\\n\\n输出格式：\\n\\n  
关键词1  
关键词2  
关键词3  
...  
关键词50  

注意：  
- 关键词应体现分类的主要需求重点，并与文档摘要内容高度相关。  
- 避免重复关键词，确保列表的多样性和完整性。  

示例:
输入分类：IT类  
输入文档摘要：
投标文档要求提供一套完整的云计算解决方案，包括服务器部署、数据库管理、网络安全防护、系统运维等服务，支持大规模并发和高可靠性需求，
同时需要详细的技术支持计划。  
输出关键词：
云计算  
服务器部署  
数据库管理  
网络安全  
系统运维  
高并发支持  
高可靠性  
技术支持  
灾备方案  
性能优化  
数据备份  
虚拟化技术  
自动化部署  
负载均衡  
服务监控  
安全加密  
访问控制  
身份认证  
技术培训  
实时监控  
数据迁移  
软件开发  
系统集成  
存储方案  
云平台  
分布式架构  
物联网支持  
人工智能集成  
边缘计算  
技术文档  
系统升级  
客户支持  
服务协议  
运维工具  
网络架构设计  
数据分析  
弹性扩展  
成本优化  
第三方接口集成  
测试方案  
故障排查  
远程支持  
项目管理  
技术评估  
研发计划  
数据恢复  
服务流程优化  
虚拟专用网络  
网络防火墙  
技术验收
"""


class KeywordListOutputParser(ListOutputParser):
    def parse(self, text: str) -> list:
        # 假设返回值是通过换行分割的列表
        return text.strip().split("\n")


generate_keywords_prompt = ChatPromptTemplate([("human", generate_keywords_template)])

generate_keywords_chain = generate_keywords_prompt | llm | KeywordListOutputParser()
