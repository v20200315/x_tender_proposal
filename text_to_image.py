from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()
prompt = """
邮件系统架构图
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
