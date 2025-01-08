from dotenv import load_dotenv

load_dotenv()

from logger_config import logger
from x_sandbox_3.graph.graph import app

if __name__ == "__main__":
    logger.info("Hello Sandbox 3")

    paths_1 = [
        "/Users/victor/myfolder/workspace-ai/x_tender_proposal/temp/tender01.pdf",
    ]

    final_summarization_1 = """
    该文档综合总结了中国移动通信集团黑龙江有限公司关于电子邮件项目的软件选型询价工作及其相关技术规范和报价要求。主要内容包括：

    1. **项目背景与参与要求**：
       - 中国移动通信集团黑龙江有限公司正在进行电子邮件项目的软件选型，邀请相关公司参与报价和技术建议书的提交，截止日期为2007年6月15日。
    
    2. **报价与技术要求**：
       - 报价需包含商务报价和技术部分，商务报价占60%，技术部分占40%。报价需详细列出产品信息、用户数及防病毒模块的相关信息。
       - 特别强调防垃圾邮件模块的报价要求、售后服务的响应时间及服务等级、代理商需提供授权文件等。
    
    3. **邮件系统功能需求**：
       - 系统应具备新用户在线申请、注册用户登录、邮件收发、管理邮件夹、邮件地址簿、邮箱使用状况查看等功能。
       - 还需支持Web日历、搜索功能、用户设置及系统维护管理等。
    
    4. **性能与安全要求**：
       - 邮件系统需具备高性能和安全性，支持大容量存储和多种操作系统，具备反垃圾邮件、病毒过滤等安全功能。
       - 性能指标要求单台邮件服务器每日处理不低于100万封邮件，支持2000个并发连接。
    
    5. **售后服务与资质要求**：
       - 售后服务需提供本地支持、响应时间承诺及产品升级维护周期。
       - 参与公司需提供相关资质证明，包括软件知识产权证书、高新技术企业认证等。
    
    6. **用户案例与硬件平台建议**：
       - 提供了多个用户案例，涵盖通信行业及中国移动的应用实例。
       - 硬件平台搭建建议包括PC服务器和小型机的配置，以满足用户需求并保证系统性能。
    
    整体而言，该文档详细阐述了电子邮件系统的技术规范、功能需求、性能指标及相关的报价和资质要求，为参与公司提供了清晰的指导。
    """

    classification_1 = "IT类"

    paths_2 = [
        "/Users/victor/myfolder/workspace-ai/x_tender_proposal/temp/tender04.pdf",
    ]

    final_summarization_2 = """
    以下是对天津市武清区财政负担经费编制外人员人事管理服务外包项目的综合总结，涵盖了主要主题：

    1. **项目概述与要求**：该项目旨在委托专业公司提供人事管理服务，涉及约1000名财政负担经费编制外人员及1600名老知青和退休人员。预算为240万元，合同履行期限为三年，供应商需符合《中华人民共和国政府采购法》的相关规定。
    
    2. **供应商资格与投标要求**：供应商需提供无重大违法记录的声明、法定代表人身份证明、营业执照等资格证明，并在《天津市政府采购网》注册为合格供应商。响应文件需在2024年12月23日09:30前提交。
    
    3. **评审标准与评分因素**：评审采用综合评分法，满分为100分，评分因素包括供应商业绩、专业化管理方案、管理规章制度、人员培训方案等。供应商需提供与项目相似的案例和详细的管理方案。
    
    4. **合同与付款条款**：合同签订后，服务期为三年，磋商保证金为20000元，需在响应文件提交截止前到账。合同草案中包括服务期限、权利义务、违约责任等条款。
    
    5. **诚信与法律责任**：供应商需对投标文件的真实性和合法性负责，提供虚假材料将面临行政处罚。参与政府采购的个人或单位如有违法行为，将被禁止参与采购活动。
    
    6. **支持中小企业政策**：文档提到政府采购中对中小企业的支持政策，包括预留采购份额和价格评审优惠等，旨在提升中小企业在政府采购中的份额。
    
    7. **响应文件提交与磋商流程**：详细说明了响应文件的编制、提交要求及磋商程序，强调了文件的规范性和提交的严谨性。供应商需提交格式规范的响应文件，包括资格证明、承诺书、声明函等。
    
    8. **质疑与投诉机制**：供应商如对成交结果有异议，可在七个工作日内提交质疑书，质疑受理部门为天津恒胜建设工程咨询有限公司，采购人和代理机构将在七个工作日内作出书面答复。
    
    9. **技术与商务要求**：供应商需提供技术方案和商务报价，确保满足项目的具体要求，并在应答中详细说明偏离情况。
    
    总体而言，该文档为潜在供应商提供了关于项目的全面信息，涵盖了参与条件、评审标准、合同条款及法律责任，确保采购过程的公正性和有效性。
    """

    classification_2 = "物业类"

    input_1 = {
        "paths": paths_1,
        "final_summarization": final_summarization_1,
        "classification": classification_1,
    }

    input_2 = {
        "paths": paths_2,
        "final_summarization": final_summarization_2,
        "classification": classification_2,
    }

    response = app.invoke(input=input_2)
