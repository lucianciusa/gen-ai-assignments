# Assignment Study Glossary - English

This glossary is written as study notes for the 02-prompt_engineering-models_parameters assignment. It explains the ideas behind the experiments, not just the parameter names.

## 1. Prompt engineering
Prompt engineering is the practice of writing instructions that make model behavior more predictable and useful. In this assignment, it means designing prompts so the output format, depth, and style match the task.

Example:
```python
prompt = "Extract the 3 main risks from the text and return valid JSON."
```

## 2. Prompt clarity
Clarity means asking for one concrete outcome in explicit language. A clear prompt reduces ambiguity and lowers the chance of off-target answers.

Example:
```python
prompt = "Summarize this article in 4 bullet points, each under 18 words."
```

## 3. Role or persona prompting
Role prompting gives the model a perspective that shapes vocabulary and tone. This is useful when the same content must be explained differently for different audiences.

Example:
```python
prompt = "You are a data science tutor for beginners. Explain overfitting in plain language."
```

## 4. Zero-shot prompting
Zero-shot means you provide a direct instruction without examples. It is fast and often enough for straightforward tasks.

Example:
```python
prompt = "Classify the sentiment as positive, neutral, or negative: 'The update is acceptable.'"
```

## 5. Few-shot prompting
Few-shot prompting includes small input-output examples to teach the pattern. It is helpful when format consistency matters.

Example:
```python
prompt = """
Input: Hola
Output: Hello
Input: Buenos dias
Output: Good morning
Input: Gracias
Output:
"""
```

## 6. Specificity in output constraints
Specificity defines length, structure, and allowed fields. It helps the model avoid generic or overlong responses.

Example:
```python
prompt = "Return a JSON object with keys: title, priority, owner. No extra text."
```

## 7. Format forcing
Format forcing is a strict request for JSON, tables, lists, or schema-like output. It supports downstream parsing and validation.

Example:
```python
prompt = "Respond only as markdown table with columns: Metric | Value | Note."
```

## 8. Context injection
Context injection provides source text or facts before the question. It reduces hallucination by grounding the model in known material.

Example:
```python
prompt = f"Based only on this policy text:\n{policy_text}\nAnswer in 3 bullets."
```

## 9. Task decomposition
Task decomposition splits a complex request into smaller stages. This usually improves control and debugging.

Example:
```python
steps = ["extract entities", "find relations", "write final summary"]
```

## 10. Iterative refinement
Iterative refinement means producing a first draft and then improving it with additional constraints. It is useful for quality tuning.

Example:
```python
prompt = "Rewrite the previous answer with a formal tone and 20% fewer words."
```

## 11. Example-based evaluation
Example-based evaluation asks the model to compare alternatives using explicit criteria. It supports rubric-driven improvement.

Example:
```python
prompt = "Score Response A and B for clarity (0-5) and pick the better one."
```

## 12. Chain-of-thought style prompting
Chain-of-thought style prompting asks for intermediate reasoning steps. In practice, it can improve difficult tasks but should be used carefully for cost and safety reasons.

Example:
```python
prompt = "Think through the trade-offs step by step, then give a final recommendation."
```

## 13. Real use case mapping
A technique is only valuable if it maps to a real problem. This assignment emphasizes selecting methods based on use-case requirements, not novelty.

Example:
```python
use_case = "structured data extraction from invoices"
```

## 14. Comparative prompting
Comparative prompting runs multiple prompt variants for the same task and compares outcomes. It helps identify the most reliable instruction style.

Example:
```python
variants = [prompt_a, prompt_b, prompt_c]
```

## 15. Reproducible experiments
Reproducibility means keeping setup, inputs, and settings explicit so results can be rerun. This is essential for fair comparisons.

Example:
```python
experiment = {"prompt": prompt, "temperature": 0.7, "top_p": 1.0}
```

## 16. Temperature
Temperature controls sampling randomness. Lower values are more deterministic, while higher values increase variety and creativity.

Example:
```python
response = client.complete(messages=messages, temperature=0.2)
```

## 17. Top-p (nucleus sampling)
Top-p keeps only the smallest token set whose cumulative probability reaches p. It is another way to control diversity.

Example:
```python
response = client.complete(messages=messages, top_p=0.9)
```

## 18. Why not tune temperature and top_p together
When both are heavily tuned at the same time, their effects can overlap and obscure interpretation. The assignment recommends isolating one variable at a time.

Example:
```python
# Keep one fixed while testing the other
settings = {"temperature": 1.0, "top_p": 0.5}
```

## 19. Presence penalty
Presence penalty discourages reusing tokens that already appeared at least once. It helps the model move to new wording or angles.

Example:
```python
response = client.complete(messages=messages, presence_penalty=0.6)
```

## 20. Frequency penalty
Frequency penalty discourages repeating tokens many times. It is useful when output becomes repetitive.

Example:
```python
response = client.complete(messages=messages, frequency_penalty=0.8)
```

## 21. Presence penalty vs frequency penalty
Presence penalty checks whether a token has appeared; frequency penalty checks how often it has appeared. They target different kinds of repetition.

Example:
```python
params = {"presence_penalty": 0.3, "frequency_penalty": 0.7}
```

## 22. Controlled prompt design
A controlled design changes one factor at a time (prompt wording or parameter value). This makes conclusions more trustworthy.

Example:
```python
baseline = {"temperature": 1.0, "top_p": 1.0}
trial = {"temperature": 0.5, "top_p": 1.0}
```

## 23. Output comparison grids
A comparison grid is a simple table that records settings and observed behavior. It helps convert intuition into evidence.

Example:
```python
rows = [{"temperature": t, "style": style_note} for t, style_note in tests]
```

## 24. Deterministic configuration
A deterministic setup prioritizes stable outputs, useful for coding tasks and structured extraction.

Example:
```python
params = {"temperature": 0.0, "top_p": 1.0}
```

## 25. Creative configuration
A creative setup increases variability for ideation, naming, or storytelling tasks.

Example:
```python
params = {"temperature": 1.1, "top_p": 0.9}
```

## 26. Max tokens
Max tokens caps response length. It prevents unnecessary verbosity and controls cost.

Example:
```python
response = client.complete(messages=messages, max_tokens=220)
```

## 27. Stop sequences
Stop sequences define strings that end generation early. They are useful for controlling boundaries in formatted outputs.

Example:
```python
response = client.complete(messages=messages, stop=["\n\n", "### END"])
```

## 28. Multiple candidates (n)
The n parameter requests several alternatives in one call. It is useful when you want to compare candidate answers quickly.

Example:
```python
response = client.complete(messages=messages, n=3)
```

## 29. Critical analysis of outputs
Critical analysis means describing what changed and why after each experiment. The assignment values interpretation, not only execution.

Example:
```python
analysis_note = "At temperature 0.0 answers were consistent but less exploratory."
```

## 30. Study takeaway
The main lesson is to connect prompting decisions and parameter settings to concrete task goals. Good results come from deliberate experimentation, not random trial and error.
