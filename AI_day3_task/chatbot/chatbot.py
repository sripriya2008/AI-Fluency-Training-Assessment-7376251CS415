from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

question = "What is the fee for AI202?"

response = client.responses.create(
    model="openai/gpt-oss-20b",
    input=question
)

print("Question:", question)
print("\nPlain LLM Answer:")
print(response.output_text)