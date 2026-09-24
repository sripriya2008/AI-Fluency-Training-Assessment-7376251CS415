from openai import OpenAI
import os
import json
from dotenv import load_dotenv

from tools import get_course_fee

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_course_fee",
            "description": "Look up the fee of a course from the private course data CSV file.",
            "parameters": {
                "type": "object",
                "properties": {
                    "course_code": {
                        "type": "string",
                        "description": "The course code, such as CS101, AI202, or DS303."
                    }
                },
                "required": ["course_code"]
            }
        }
    }
]

question = "What is the fee for AI202?"

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful course information assistant. Use the course fee tool when the user asks for a course fee."
        },
        {
            "role": "user",
            "content": question
        }
    ],
    tools=tools,
    tool_choice="auto"
)

message = response.choices[0].message

print("Question:", question)

if message.tool_calls:
    for tool_call in message.tool_calls:
        print("\nTool Call:")
        print("Tool:", tool_call.function.name)
        print("Arguments:", tool_call.function.arguments)

        arguments = json.loads(tool_call.function.arguments)

        result = get_course_fee(arguments["course_code"])

        print("\nTool Result:")
        print(result)

        final_response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful course information assistant."
                },
                {
                    "role": "user",
                    "content": question
                },
                message,
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result
                }
            ]
        )

        print("\nFinal Answer:")
        print(final_response.choices[0].message.content)

else:
    print("\nNo tool was called.")
    print("\nAnswer:")
    print(message.content)