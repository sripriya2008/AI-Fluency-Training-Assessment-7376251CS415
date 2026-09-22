# Student Study Assistant - Chatbot vs Workflow vs AI Agent

## Project Overview

This project compares three approaches for solving the same problem:

1. Plain Chatbot
2. Rule-Based Workflow
3. AI Agent

The selected scenario is a Student Study Assistant.

The system uses a student's study data to help determine what subject the student should study next.

## Private Data

The private study data is stored in:

`data/study_data.csv`

It contains:

- Subject
- Progress
- Pending Topic
- Priority

## 1. Plain Chatbot

The plain chatbot provides general study advice.

It does not directly access the student's private study data.

Run:

```bash
python chatbot/chatbot.py