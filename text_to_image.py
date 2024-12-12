from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()
prompt = """
An email system architecture diagram for a tender project, showing the overall system architecture including mail 
servers, gateways, storage systems, and user terminals. The diagram should highlight the connection between these 
modules and indicate the functionality and data flow paths. The design should be clean, professional, and easy to 
understand, with clear labels and arrows demonstrating how data flows through the system. The diagram must convey 
a clear understanding of the system's operational mechanisms, suitable for inclusion in a formal project proposal 
for a bidding process.
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
