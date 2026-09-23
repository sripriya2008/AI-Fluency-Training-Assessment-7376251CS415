import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Tool: calculate remaining study time
def calculate_remaining_time(total_hours, python_hours, dbms_hours):
    remaining = total_hours - (python_hours + dbms_hours)
    return remaining


question = """
A student has 6 hours available for studying.
They spend 2 hours on Python and 1.5 hours on DBMS.
How many hours are remaining?
"""

# ReAct-style process
print("Question:")
print(question)

print("\nAction:")
print("Using the calculate_remaining_time tool...")

result = calculate_remaining_time(6, 2, 1.5)

print("\nObservation:")
print(f"The tool calculated {result} hours remaining.")

prompt = f"""
Answer the user's question using this tool result.

Question:
{question}

Tool result:
{result} hours remaining.

Give a short explanation and final answer.
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

print("\nFinal Answer:")
print(response.choices[0].message.content)