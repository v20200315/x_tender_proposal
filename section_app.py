from dotenv import load_dotenv

from x_section.graph.graph import app

load_dotenv()

if __name__ == "__main__":
    print("Hello Tender Proposal x_content")
    paths = [
        "/Users/victor/myfolder/workspace-ai/x_tender_proposal/temp/temp.pdf",
    ]
    project_name = "中国移动通信集团黑龙江有限公司-电子邮件系统-技术方案建议书"
    input_texts = ["方案综述-项目背景", "方案综述-项目的建设目标"]
    min_length = 300
    result = app.invoke(
        input={
            "paths": paths,
            "project_name": project_name,
            "input_texts": input_texts,
            "min_length": min_length,
        }
    )
