import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

question = """
A student has 6 hours available for studying.
They spend 2 hours on Python and 1.5 hours on DBMS.
How many hours are remaining?
"""

prompt = f"""
Solve the following problem carefully.

Give a short reasoning summary showing the calculation,
then give the final answer.

Question:
{question}
"""

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0
)

print("Question:")
print(question)

print("Chain-of-Thought Answer:")
print(response.choices[0].message.content)