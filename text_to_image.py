from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()
prompt = """
邮件服务器集群部署图 \n
该图展示了多台邮件服务器通过负载均衡器连接的结构。
每台服务器都配置有冗余硬件，确保高可用性。负载均衡器负责将用户请求分配到不同的服务器上，以实现负载均衡。
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
