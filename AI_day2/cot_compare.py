import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'AI')))

from config import client, MODEL

QUESTIONS = [
    "The fees of 3 courses are ₹12,000, ₹18,000, and ₹15,000. "
    "A 15% scholarship is given. The remaining amount is paid in 4 instalments. "
    "How much is each instalment?",

    "A computer lab has 18 computers. "
    "Each computer can be used by 2 students in the morning and 3 students in the afternoon. "
    "How many student sittings are available in total?",

    "Ravi is taller than Kumar. Kumar is taller than Arun. "
    "Priya is shorter than Arun. Who is the tallest and who is the shortest?"
]


DIRECT_PROMPT = """
You are a helpful assistant.
Give only the final answer.
Do not explain.
"""


COT_PROMPT = """
You are a helpful assistant.
Solve the problem step by step.
Number each step and show the calculation in that step.
After the steps, write the last line exactly as:

Final Answer: <answer>
"""


def ask(question, prompt):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": prompt
            },
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content


for i, question in enumerate(QUESTIONS, start=1):

    print("\n" + "=" * 60)
    print("QUESTION", i)
    print(question)

    print("\n--- WITHOUT CoT ---")
    print(ask(question, DIRECT_PROMPT))

    print("\n--- WITH CoT ---")
    print(ask(question, COT_PROMPT))