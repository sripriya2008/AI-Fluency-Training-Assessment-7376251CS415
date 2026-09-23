import os
from collections import Counter
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

question = """
A student has 10 hours available for studying.
They spend 3 hours on Python, 2 hours on DBMS,
and 1 hour on C++.
How many hours are remaining?
"""

def get_answer(temperature):
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": f"""
Solve this problem and give only the final numerical answer
with the unit.

Question:
{question}
"""
            }
        ],
        temperature=temperature
    )

    return response.choices[0].message.content.strip()


print("Question:")
print(question)

print("\n--- Multiple Runs (Temperature = 0.7) ---")

answers = []

for i in range(5):
    answer = get_answer(0.7)
    answers.append(answer)
    print(f"Run {i + 1}: {answer}")

print("\n--- Majority Result ---")

counts = Counter(answers)
majority_answer, count = counts.most_common(1)[0]

print(f"Most common answer: {majority_answer}")
print(f"Occurrences: {count}/5")

print("\n--- Temperature = 0 ---")

answer_zero = get_answer(0)
print(f"Temperature 0 answer: {answer_zero}")