# Reasoning and Acting: Comparing Direct Prompting, Chain-of-Thought, and ReAct

## 1. Scenario

This project uses a Student Study Assistant scenario.

The main task is to determine how much study time remains after a student spends time on different subjects.

Example question:

> A student has 6 hours available for studying.
> They spend 2 hours on Python and 1.5 hours on DBMS.
> How many hours are remaining?

The correct answer is 2.5 hours.

The project also demonstrates self-consistency using a separate reasoning question.

---

## 2. Direct Prompting

Direct Prompting gives the model the question directly without asking it to use a tool or follow a specific reasoning process.

### Process

Question → AI Model → Final Answer

### Result

The model calculated:

6 - (2 + 1.5) = 2.5 hours

Final answer: 2.5 hours.

### What it can do

- Answer simple questions quickly.
- Perform basic calculations.
- Work without external tools.

### Limitations

- It does not automatically use external tools.
- For complex multi-step tasks, errors may occur.
- There is less control over the reasoning process.

---

## 3. Chain-of-Thought

The Chain-of-Thought approach asks the model to solve the problem carefully and provide a short reasoning summary before the final answer.

### Process

Question → Reasoning Summary → Final Answer

### Result

The model identified:

- Total time = 6 hours
- Python = 2 hours
- DBMS = 1.5 hours
- Used time = 3.5 hours
- Remaining time = 2.5 hours

Final answer: 2.5 hours.

### What it can do

- Break a problem into intermediate steps.
- Make calculations easier to follow.
- Help with multi-step reasoning tasks.

### Limitations

- It still does not automatically access external information.
- More generated text can increase response time and token usage.
- A reasoning explanation does not guarantee that the answer is correct.

---

## 4. ReAct

ReAct combines reasoning with actions. In this project, a calculator-style tool was used to calculate the remaining study time.

### Process

Question → Action → Tool → Observation → Final Answer

### Result

The tool calculated:

6 - (2 + 1.5) = 2.5 hours

The model then used the tool result to produce the final answer.

### What it can do

- Use external tools or functions.
- Combine tool results with reasoning.
- Handle tasks where information must be obtained or calculated using a tool.

### Limitations

- Requires tools to be available and correctly implemented.
- Tool errors can affect the final result.
- More steps can make the process slower than direct prompting.

---

## 5. Comparison

| Feature | Direct Prompting | Chain-of-Thought | ReAct |
|---|---|---|---|
| Reasoning depth | Basic | More structured | Reasoning + actions |
| Tool usage | No | No | Yes |
| Multi-step questions | Can handle simple ones | Better suited | Useful when tools are needed |
| Transparency | Final response | Reasoning summary | Action and observation can be shown |
| Speed/Cost | Usually lower | Can use more tokens | Can require additional tool calls |
| Consistency | Depends on model | Depends on model | Depends on model and tools |

---

## 6. Self-Consistency Experiment

A separate question was used:

> A student has 10 hours available for studying.
> They spend 3 hours on Python, 2 hours on DBMS, and 1 hour on C++.
> How many hours are remaining?

Correct calculation:

10 - (3 + 2 + 1) = 4 hours.

Five runs were performed with temperature 0.7.

### Results

| Run | Answer |
|---|---|
| 1 | 4 hours |
| 2 | 4 hours |
| 3 | 4 hours |
| 4 | 4 hours |
| 5 | 4 hours |

All five runs produced the same answer.

The majority answer was therefore 4 hours.

A separate run with temperature 0 also produced 4 hours.

### Observation

For this simple arithmetic problem, changing the temperature did not change the final answer in the experiment.

Self-consistency can be useful for reasoning tasks because multiple independent outputs can be compared. If different answers are produced, the most frequent answer can be used as one signal for selecting an answer, although frequency alone does not guarantee correctness.

---

## 7. Suitability Analysis

### Direct Prompting

Suitable for:
- Simple questions
- Fast answers
- Straightforward calculations
- Tasks that do not require external information

### Chain-of-Thought

Suitable for:
- Multi-step reasoning
- Problems requiring intermediate calculations
- Situations where a reasoning summary helps explain the result

### ReAct

Suitable for:
- Tasks requiring tools
- External information retrieval
- Calculations or actions performed by functions
- Multi-step tasks involving observations from tools

---

## 8. Conclusion

The three approaches solve problems in different ways.

Direct Prompting sends the question directly to the model and is simple and fast.

Chain-of-Thought encourages structured reasoning and can be useful for multi-step problems.

ReAct adds tool usage to the reasoning process, making it useful when the task requires an external tool or action.

The experiments show that the appropriate approach depends on the type of task. Simple questions can be handled directly, reasoning-heavy questions can benefit from structured reasoning, and tasks requiring external information or actions can benefit from a tool-based approach.