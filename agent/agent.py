import json
import os

from groq import Groq
from tools import read_study_data


# --------------------------------------------------
# GROQ CLIENT
# --------------------------------------------------

client = Groq(
    api_key=os.getenv("OPENAI_API_KEY")
)


print("====================================")
print("             AI AGENT")
print("====================================")

print()

user_question = input("You: ")

print()


# --------------------------------------------------
# TOOL DEFINITION
# --------------------------------------------------

def study_data_tool():
    """Read the student's private study data."""
    return read_study_data()


tools = [
    {
        "type": "function",
        "function": {
            "name": "read_study_data",
            "description": (
                "Read the student's private study data "
                "from the study CSV file."
            ),
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    }
]


# --------------------------------------------------
# INITIAL MESSAGE
# --------------------------------------------------

messages = [
    {
        "role": "system",
        "content": (
            "You are a student study assistant. "
            "When the user asks about their study progress "
            "or what they should study next, use the "
            "read_study_data tool first. "
            "After receiving the private study data, "
            "analyze it and give a clear recommendation."
        )
    },
    {
        "role": "user",
        "content": user_question
    }
]


# --------------------------------------------------
# FIRST LLM CALL
# --------------------------------------------------

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=messages,
    tools=tools,
    tool_choice="auto"
)


assistant_message = response.choices[0].message


# --------------------------------------------------
# CHECK WHETHER LLM REQUESTED THE TOOL
# --------------------------------------------------

if assistant_message.tool_calls:

    print("Agent decided to use tool:")
    print("read_study_data()")
    print()

    # Add assistant's tool request to conversation
    messages.append(assistant_message)

    # Execute the requested tool
    study_data = study_data_tool()

    print("Tool result:")
    print(json.dumps(study_data, indent=2))
    print()

    # Send tool result back to the LLM
    for tool_call in assistant_message.tool_calls:

        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(study_data)
            }
        )


    # --------------------------------------------------
    # SECOND LLM CALL
    # --------------------------------------------------

    final_response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=messages,
        tools=tools
    )

    final_answer = final_response.choices[0].message.content

    print("Agent:")
    print(final_answer)


else:

    print("Agent:")
    print(assistant_message.content)