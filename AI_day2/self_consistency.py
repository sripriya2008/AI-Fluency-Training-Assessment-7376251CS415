from collections import Counter

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'AI')))

from config import client, MODEL


QUESTION = (
    "The fees of 3 courses are ₹12,000, ₹18,000, and ₹15,000. "
    "A 15% scholarship is given. The remaining amount is paid in 4 instalments. "
    "How much is each instalment?"
)

COT_PROMPT = """
You are a helpful assistant.
Solve the problem step by step.
Number each step and show the calculation in that step.
After the steps, write the last line exactly as:

Final Answer: <answer>
"""

RUNS = 5
TEMPERATURE = 0.8


answers = []

for i in range(RUNS):

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": COT_PROMPT
            },
            {
                "role": "user",
                "content": QUESTION
            }
        ],
        temperature=TEMPERATURE
    )

    result = response.choices[0].message.content

    print("\nRUN", i + 1)
    print(result)

    if "Final Answer:" in result:
        answer = result.split("Final Answer:")[-1].strip()
        answers.append(answer)


print("\n" + "=" * 50)
print("ANSWERS:")
for answer in answers:
    print(answer)


if answers:
    counts = Counter(answers)
    majority_answer, count = counts.most_common(1)[0]

    print("\nMAJORITY ANSWER:", majority_answer)
    print("COUNT:", count, "/", RUNS)