# Reasoning and Acting: Direct Prompting, Chain-of-Thought, and ReAct

This project compares three AI approaches for solving a student study-planning problem:

1. Direct Prompting
2. Chain-of-Thought
3. ReAct

It also demonstrates Self-Consistency using multiple model runs.

## Project Structure

- `direct_prompting/` - Direct prompting implementation
- `chain_of_thought/` - Chain-of-Thought implementation
- `react/` - ReAct implementation with a tool
- `self_consistency/` - Self-Consistency experiment
- `output/` - Screenshots of the experiments
- `analysis.md` - Detailed analysis and comparison

## Model

The project uses the Groq API with:

`openai/gpt-oss-120b`

## Main Scenario

A student has a fixed amount of study time and spends time studying different subjects. The programs calculate the remaining study time using different AI approaches.

## Requirements

Install the required packages using:

```bash
python -m pip install -r ../requirements.txt