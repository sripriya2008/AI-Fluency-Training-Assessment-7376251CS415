# From Prompt to Action: Understanding LLMs, Tools, and Agents

## 1. Scenario

For this project, I chose a course-fee lookup scenario.

I created a private CSV file named `course_data.csv`. It contains course codes, course names, and course fees.

Example data:

| Course Code | Course Name | Fee |
|---|---|---:|
| CS101 | Programming Fundamentals | Rs.15000 |
| AI202 | Artificial Intelligence | Rs.18000 |
| DS303 | Data Science | Rs.20000 |

The main question used in the demonstration is:

> What is the fee for AI202?

This scenario shows the difference between a plain LLM and an LLM that has access to one external tool.

---

# 2. Explanation of Concepts

## 2.1 What is a Large Language Model?

A Large Language Model, or LLM, is an AI model trained on a large amount of text. It can understand a user's question and generate a natural-language answer.

For example, if I ask:

> What is artificial intelligence?

The LLM can answer from its general knowledge without needing an external tool.

However, a plain LLM does not automatically have access to my private `course_data.csv` file. Therefore, if I ask:

> What is the fee for AI202?

the model cannot reliably read my CSV file and find the exact fee.

In my experiment, the plain LLM answered:

> I’m not sure which “AI202” you’re referring to...

It asked for more information instead of giving the value from my private CSV file.

This demonstrates an important limitation. An LLM can generate an answer from its learned knowledge, but it cannot automatically access new private data or perform an external operation unless that capability is provided.

---

## 2.2 What is an Agent?

An AI agent is an LLM connected to tools and given the ability to decide when a tool is needed and use its result.

In my scenario, the plain LLM receives:

> What is the fee for AI202?

and produces an answer using only the conversation and its own knowledge.

The tool-enabled agent receives the same question, but it also knows about a tool called `get_course_fee`.

The agent can recognize that the exact course fee is stored in a private CSV file. It can call the tool, receive the result, and then use that result to produce the final answer.

Therefore, the important difference is that an agent can connect the LLM's reasoning with an external action.

---

## 2.3 What is a Tool?

A tool is an external function that gives an LLM an ability that it does not have by itself.

In this project, my tool is:

`get_course_fee`

It reads `course_data.csv` and finds the fee for a requested course code.

For example:

`get_course_fee("AI202")`

returns the course information and fee.

The tool allows the LLM to access the private course information instead of trying to guess the answer.

---

## 2.4 What is a Tool Call?

A tool call happens when the LLM decides that it needs to use a particular tool and sends the required arguments to that tool.

For example, for the question:

> What is the fee for AI202?

the model can produce a tool call similar to:

```text
Tool: get_course_fee
Arguments: {"course_code": "AI202"}