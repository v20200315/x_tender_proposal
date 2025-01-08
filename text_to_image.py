from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()
prompt = """
绘制一张详细的邮件系统架构示意图，图中包括以下组件：

顶部有一个云状图标，标注为“Internet”，连接到一个路由器。
路由器连接到一个防火墙，随后连接到中心的交换机。
交换机连接到以下部分：
左侧为两个客户端，分别标注为“外网邮件客户端”和“内网邮件客户端”。
中间是一个 DMZ 区域，包含一个负载均衡器和多台服务器，标注为“MTA/MMP/Web Proxy”。
下方是一个安全网络段，由防火墙保护，包含两台集群服务器，标注为“T2000”。
集群服务器提供以下功能：
“消息存储（Message Store）”
“LDAP目录服务”
“POP服务”
“IMAP服务”
集群服务器连接到一个“磁盘阵列”。
请使用清晰的线条、标注箭头表示连接关系，整体布局简洁有条理，并使用现代化的配色方案，使图表易于理解且具有专业感。(图片中不要有文字)
"""

client = OpenAI()

response = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="1024x1024",
    quality="standard",
    n=1,
)

image_url = response.data[0].url

print("Generated image URL:", image_url)
