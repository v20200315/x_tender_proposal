import json
import os
import streamlit as st
from x_outline_v2.graph.graph import app

json_str = """
{
    "title": "电子邮件项目投标书大纲",
    "sections": [
        {
            "title": "1 项目概述",
            "abstract": "介绍中国移动通信集团黑龙江有限公司电子邮件项目的背景、需求和参与要求。",
            "subsections": [
                {
                    "title": "1.1 项目背景",
                    "abstract": "概述项目的发起原因及其在中国移动通信集团黑龙江有限公司中的重要性。"
                },
                {
                    "title": "1.2 需求分析",
                    "abstract": "详细描述项目的核心需求，包括用户数、防病毒和防垃圾模块等技术要求。",
                    "subsections": [
                        {
                            "title": "1.2.1 用户需求",
                            "abstract": "分析用户数量及其对系统功能的具体需求。"
                        },
                        {
                            "title": "1.2.2 技术要求",
                            "abstract": "描述防病毒和防垃圾模块的技术规格和性能要求。"
                        }
                    ]
                },
                {
                    "title": "1.3 参与要求",
                    "abstract": "列出参与公司的资格要求和提交材料的具体细节。",
                    "subsections": [
                        {
                            "title": "1.3.1 资格要求",
                            "abstract": "说明参与公司需具备的资质和经验。"
                        },
                        {
                            "title": "1.3.2 提交材料",
                            "abstract": "列出需提交的文件和材料清单。"
                        }
                    ]
                }
            ]
        },
        {
            "title": "2 技术规范",
            "abstract": "概述邮件系统的设计要求、功能需求及性能指标，涵盖前端应用和维护管理需求。",
            "subsections": [
                {
                    "title": "2.1 前端应用需求",
                    "abstract": "描述用户在线申请、邮件收发、邮箱设置等前端功能需求。",
                    "subsections": [
                        {
                            "title": "2.1.1 用户注册与登录",
                            "abstract": "介绍新用户在线申请和注册用户登录的流程。"
                        },
                        {
                            "title": "2.1.2 邮件处理功能",
                            "abstract": "描述邮件收发、邮件夹管理和地址簿功能。"
                        },
                        {
                            "title": "2.1.3 邮箱设置",
                            "abstract": "说明邮箱设置选项，包括密码、过滤规则和签名设置。"
                        }
                    ]
                },
                {
                    "title": "2.2 维护管理需求",
                    "abstract": "涵盖系统监控、日志管理及防垃圾邮件模块的管理需求。",
                    "subsections": [
                        {
                            "title": "2.2.1 系统监控",
                            "abstract": "描述系统监控和日志管理的功能。"
                        },
                        {
                            "title": "2.2.2 安全管理",
                            "abstract": "介绍防垃圾邮件和防病毒模块的管理要求。"
                        }
                    ]
                },
                {
                    "title": "2.3 性能指标",
                    "abstract": "列出系统需满足的性能指标，如邮件处理能力和安全性要求。",
                    "subsections": [
                        {
                            "title": "2.3.1 处理能力",
                            "abstract": "说明系统的邮件处理速度和用户支持能力。"
                        },
                        {
                            "title": "2.3.2 安全性",
                            "abstract": "描述系统的安全设计和身份认证机制。"
                        }
                    ]
                }
            ]
        },
        {
            "title": "3 系统功能",
            "abstract": "描述邮件系统支持的多种客户端功能、邮件管理和用户设置选项。",
            "subsections": [
                {
                    "title": "3.1 客户端支持",
                    "abstract": "介绍系统对多种邮件客户端和Web邮箱的支持情况。",
                    "subsections": [
                        {
                            "title": "3.1.1 邮件客户端",
                            "abstract": "描述系统对Outlook、Foxmail等客户端的支持。"
                        },
                        {
                            "title": "3.1.2 Web邮箱",
                            "abstract": "说明Web邮箱的功能和用户体验。"
                        }
                    ]
                },
                {
                    "title": "3.2 邮件管理功能",
                    "abstract": "详细说明邮件收发、自动回执、定时发送等管理功能。",
                    "subsections": [
                        {
                            "title": "3.2.1 收发功能",
                            "abstract": "介绍邮件收发、备份和草稿保存功能。"
                        },
                        {
                            "title": "3.2.2 自动化功能",
                            "abstract": "描述自动回执、定时发送和邮件优先级设置。"
                        }
                    ]
                },
                {
                    "title": "3.3 用户设置选项",
                    "abstract": "描述用户可进行的邮箱设置，包括密码管理和过滤规则。",
                    "subsections": [
                        {
                            "title": "3.3.1 安全设置",
                            "abstract": "说明密码管理和安全设置选项。"
                        },
                        {
                            "title": "3.3.2 过滤规则",
                            "abstract": "介绍邮件过滤规则的设置和管理。"
                        }
                    ]
                }
            ]
        },
        {
            "title": "4 性能与安全",
            "abstract": "详细说明邮件系统和网关系统的性能需求、安全设计及管理功能。",
            "subsections": [
                {
                    "title": "4.1 性能需求",
                    "abstract": "概述邮件系统和网关系统的处理能力和资源使用要求。",
                    "subsections": [
                        {
                            "title": "4.1.1 系统处理能力",
                            "abstract": "描述系统的邮件处理速度和并发连接能力。"
                        },
                        {
                            "title": "4.1.2 资源使用",
                            "abstract": "说明系统在正常运行时的CPU和内存使用情况。"
                        }
                    ]
                },
                {
                    "title": "4.2 安全设计",
                    "abstract": "描述系统的安全功能，包括反垃圾邮件和身份认证机制。",
                    "subsections": [
                        {
                            "title": "4.2.1 反垃圾邮件",
                            "abstract": "介绍反垃圾邮件功能和查杀率要求。"
                        },
                        {
                            "title": "4.2.2 身份认证",
                            "abstract": "说明身份认证机制和用户信息安全措施。"
                        }
                    ]
                },
                {
                    "title": "4.3 管理功能",
                    "abstract": "介绍系统的实时监控、日志管理和连接控制功能。",
                    "subsections": [
                        {
                            "title": "4.3.1 实时监控",
                            "abstract": "描述系统的实时监控和邮件队列管理功能。"
                        },
                        {
                            "title": "4.3.2 连接控制",
                            "abstract": "说明连接控制的设置和管理。"
                        }
                    ]
                }
            ]
        },
        {
            "title": "5 售后服务与资质",
            "abstract": "列出售后服务承诺、用户案例及相关资质要求，确保项目的可靠性和支持能力。",
            "subsections": [
                {
                    "title": "5.1 售后服务承诺",
                    "abstract": "详细说明售后服务的响应时间和支持能力。",
                    "subsections": [
                        {
                            "title": "5.1.1 响应时间",
                            "abstract": "说明售后服务的响应时间承诺。"
                        },
                        {
                            "title": "5.1.2 支持能力",
                            "abstract": "描述本地服务支持和人员的二次开发能力。"
                        }
                    ]
                },
                {
                    "title": "5.2 用户案例",
                    "abstract": "列举在通信行业的成功应用案例，展示系统的可靠性。",
                    "subsections": [
                        {
                            "title": "5.2.1 通信行业案例",
                            "abstract": "介绍在通信行业的具体应用案例。"
                        },
                        {
                            "title": "5.2.2 中国移动案例",
                            "abstract": "描述在中国移动及其子公司的应用情况。"
                        }
                    ]
                },
                {
                    "title": "5.3 资质要求",
                    "abstract": "列出参与公司需具备的资质证明和认证文件。",
                    "subsections": [
                        {
                            "title": "5.3.1 资质证明",
                            "abstract": "说明注册资本复印件和系统集成资质的要求。"
                        },
                        {
                            "title": "5.3.2 认证文件",
                            "abstract": "列出涉密认证和高新技术企业认证的必要性。"
                        }
                    ]
                }
            ]
        }
    ]
}
"""

st.set_page_config(page_title="投标文件生成器")
st.markdown("#### 投标文件Outline生成器 V0.1.2")


# 初始化状态
if "button_enabled" not in st.session_state:
    st.session_state["button_enabled"] = True
if "processing" not in st.session_state:
    st.session_state["processing"] = False

uploaded_file = st.file_uploader(
    "相关文档（暂时只支持上传一个PDF格式的文件）",
    type="pdf",
    accept_multiple_files=False,
)


def handle_click():
    st.session_state["button_enabled"] = False
    st.session_state["processing"] = True


# 按钮逻辑
button_clicked = st.button(
    "生成",
    disabled=not st.session_state["button_enabled"],
    on_click=handle_click,
)

# 执行业务逻辑
if st.session_state.processing:
    st.session_state["button_enabled"] = True
    st.session_state["processing"] = False

    if not uploaded_file:
        st.info("请上传相关文档，用于生成更加完整合理的信息。")
        st.stop()

    # 定义存放文件的目录
    output_dir = "temp"
    os.makedirs(output_dir, exist_ok=True)  # 创建目录，如果已存在则不会报错

    with st.spinner("AI正在思考中，请稍等..."):
        file_content = uploaded_file.read()
        temp_file_path = os.path.join(output_dir, "temp.pdf")
        with open(temp_file_path, "wb") as temp_file:
            temp_file.write(file_content)

        with st.container(height=500):
            st.write("Outline")
            response = app.invoke(input={"paths": [temp_file_path]})
            json_data = json.dumps(response["outline"], indent=4, ensure_ascii=False)
            st.code(json_data, wrap_lines=True, language="json")

            # parsed_json = json.loads(json_str)
            # formatted_json = json.dumps(parsed_json, indent=4, ensure_ascii=False)
            # st.code(formatted_json, wrap_lines=True, language="json")