# Comparing a Plain Chatbot, Rule-Based Workflow, and AI Agent

## 1. Scenario

### Student Study Assistant

The selected scenario is a Student Study Assistant.

The system helps a student decide what subject to study next based on their study progress, pending topics, and priority.

The private study data is stored in:

`data/study_data.csv`

The data contains:

| Subject | Progress | Pending Topic | Priority |
| ------- | -------: | ------------- | -------- |
| Python  |      70% | Functions     | High     |
| DBMS    |      60% | Joins         | High     |
| C++     |      80% | Trees         | Medium   |
| German  |      50% | Accusative    | Low      |

The same problem is implemented using three different approaches:

1. Plain Chatbot
2. Rule-Based Workflow
3. AI Agent

---

# 2. Private Data

The student's study information is considered private data.

The CSV file contains:

* Subject
* Progress percentage
* Pending topic
* Priority

The three approaches handle this private data differently.

---

# 3. Plain Chatbot

## Implementation

The plain chatbot provides general study-related responses.

It does not directly access the student's private CSV file.

For example, when the user asks:

> What should I study next?

the chatbot explains that it cannot access the student's private study information and can only provide general advice.

## Data Access

The chatbot does not have direct access to:

`data/study_data.csv`

Therefore, it cannot make a personalized recommendation using the student's actual progress.

## Tools and Rules

No external tool is used.

There is also no private-data processing.

The response is mainly based on the user's question and the chatbot's general knowledge.

## Request Handling

The chatbot receives the user's question and generates a general response.

## Limitation

The main limitation is that it cannot automatically use the student's private study information.

Therefore, its recommendation may be generic.

---

# 4. Rule-Based Workflow

## Implementation

The rule-based workflow directly reads the student's CSV file.

It uses a predefined rule:

**Priority = High AND Progress < 70%**

If a subject satisfies this condition, it is recommended.

With the current data:

* Python → 70%, High
* DBMS → 60%, High
* C++ → 80%, Medium
* German → 50%, Low

DBMS satisfies the predefined rule.

Therefore, the workflow recommends DBMS.

## Data Access

The workflow directly reads:

`data/study_data.csv`

It can access the private data because the program has been specifically written to read the file.

## Tools and Rules

The workflow uses:

* CSV file reading
* `if` condition
* Predefined decision rule

## Request Handling

The workflow follows a fixed sequence:

1. Read the CSV file.
2. Read subject information.
3. Check progress.
4. Check priority.
5. Apply the predefined rule.
6. Produce a recommendation.

## Limitation

The workflow is predictable but not very flexible.

If the user asks a question that requires a different type of reasoning, the predefined rule may not be sufficient.

For example, changing the rule may require modifying the program code.

---

# 5. AI Agent

## Implementation

The AI agent combines:

* Large Language Model (LLM)
* Tool
* Private data
* Multi-step processing

The agent has access to a tool called:

`read_study_data()`

This tool reads the student's private CSV file.

## Data Access

The AI agent does not simply place the CSV data directly inside the prompt.

Instead, the agent can request the `read_study_data()` tool.

The tool reads the private data and returns the result to the agent.

## Request Handling

For a question such as:

> What should I study next?

the process is:

1. User sends the question.
2. LLM analyzes the request.
3. LLM decides that private study data is required.
4. LLM requests the `read_study_data()` tool.
5. The program executes the tool.
6. The private study data is returned.
7. The data is provided back to the LLM.
8. The LLM analyzes the information.
9. The agent gives a personalized response.

This demonstrates a multi-step agent workflow.

## Tools

The main tool is:

`read_study_data()`

Its purpose is to safely retrieve the student's study information from the CSV file.

## Limitation

Because the agent uses an LLM, its final interpretation can be less predictable than a fixed rule.

The tool and private-data access also need to be properly controlled to prevent inappropriate data access.

---

# 6. Comparison

| Basis               | Plain Chatbot                                                     | Rule-Based Workflow              | AI Agent                                                   |
| ------------------- | ----------------------------------------------------------------- | -------------------------------- | ---------------------------------------------------------- |
| Flexibility         | High for conversation, but no private data in this implementation | Low because rules are predefined | High because the LLM can adapt to different requests       |
| Decision-making     | Generates a general response                                      | Uses fixed `if/else` rules       | LLM analyzes the request and can decide when to use a tool |
| Tool usage          | No tool                                                           | Direct CSV/file processing       | Uses `read_study_data()` as a tool                         |
| Private-data access | No direct access                                                  | Directly reads CSV               | Accesses CSV through a tool                                |
| Multi-step handling | Limited                                                           | Fixed sequence                   | Can perform multiple steps involving LLM and tools         |
| Automation          | Low for personalized study decisions                              | High for fixed decisions         | High for flexible personalized tasks                       |
| Reliability         | General responses may not use private information                 | Predictable for predefined rules | Flexible, but LLM-generated decisions can vary             |

---

# 7. Suitability Analysis

## Plain Chatbot

A plain chatbot is suitable when the user needs:

* General explanations
* General study advice
* Conversational interaction
* Information that does not require private data

It is less suitable when the response depends on the student's private study information.

## Rule-Based Workflow

A rule-based workflow is suitable when:

* The decision rules are clearly known.
* The conditions do not change frequently.
* Predictable results are important.
* The task is simple.

For example, a college could use fixed rules to identify subjects whose progress is below a particular threshold.

## AI Agent

An AI agent is suitable when:

* The user can ask different types of questions.
* Private data needs to be retrieved through tools.
* Multiple steps are required.
* The system needs flexible reasoning.
* Different tools may be needed for different requests.

For example, a future version could use separate tools for study progress, assignments, attendance, and exam schedules.

---

# 8. General Conclusion

The three approaches solve the same general problem in different ways.

A **plain chatbot** is useful for general conversation and advice but does not automatically use the student's private data in this implementation.

A **rule-based workflow** provides predictable decisions using predefined rules. It is simple and effective when the requirements are fixed.

An **AI agent** combines an LLM with tools and private-data access. It can handle a more flexible request by deciding when to use a tool, receiving the result, and continuing the reasoning process.

Therefore, the appropriate approach depends on the requirements of the problem:

* Use a plain chatbot for general conversational assistance.
* Use a rule-based workflow for fixed and predictable decisions.
* Use an AI agent for flexible, multi-step tasks that require tools and private data.
