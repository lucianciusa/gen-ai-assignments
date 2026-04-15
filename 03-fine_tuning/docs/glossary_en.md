# Assignment Study Glossary - English

This glossary summarizes the key concepts learned in Assignment 3 (fine-tuning + stored completions workflow) and explains them as study notes.

## 1. Fine-tuning
Fine-tuning is the process of adapting a base model to a specific task, tone, or domain using curated examples.

Example:
```python
# Train a model specialized in Azure support responses
```

## 2. Base model
The base model is the original pretrained deployment used as a starting point before custom training.

Example:
```python
BASE_DEPLOYMENT_NAME = "gpt-4o-mini"
```

## 3. Fine-tuned model
A fine-tuned model is the trained result produced from the base model plus your dataset.

Example:
```python
FINETUNED_DEPLOYMENT_NAME = "gpt-4o-mini-...ft-azure-support-v1"
```

## 4. Distilled model
In this assignment, distillation is used to produce a compact specialized variant and compare it against the base model.

Example:
```python
DISTILLED_DEPLOYMENT_NAME = "gpt-4o-mini-...ft-distilled"
```

## 5. Training set
The training set contains most examples and is used to update model parameters during fine-tuning.

Example:
```text
stored_completions_training_set.jsonl
```

## 6. Validation set
The validation set is held out from training and used to estimate generalization quality.

Example:
```text
stored_completions_validation_set.jsonl
```

## 7. JSONL format
JSONL (JSON Lines) stores one JSON object per line. It is required for chat fine-tuning datasets.

Example:
```json
{"messages": [{"role": "system", "content": "..."}, {"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}]}
```

## 8. Chat messages schema
Each training sample must follow chat structure with roles and textual content.

Example:
```python
{"role": "user", "content": "How do I deploy a fine-tuned model?"}
```

## 9. Role normalization
Only valid roles should be kept (`system`, `user`, `assistant`) during dataset sanitization.

Example:
```python
allowed_roles = {"system", "user", "assistant"}
```

## 10. Content normalization
Message content can arrive in different shapes and should be normalized to plain text for training compatibility.

Example:
```python
content = _normalize_message_content(value)
```

## 11. Schema sanitization
Schema sanitization removes invalid fields and keeps only what the trainer expects.

Example:
```python
cleaned.append({"role": role, "content": content})
```

## 12. Stored completions
Stored completions capture real model interactions that can later be transformed into retraining datasets.

Example:
```python
client.chat.completions.create(..., store=True)
```

## 13. Traffic generation
Traffic generation creates diverse requests so stored logs contain enough usable examples.

Example:
```python
total_calls = 120
```

## 14. Metadata tagging
Metadata tags help categorize captured interactions for filtering and analysis.

Example:
```python
metadata={"category": "fine-tuning-assignment", "batch": "notebook-2"}
```

## 15. REST extraction
Stored completions can be extracted through REST endpoints with authenticated requests.

Example:
```python
requests.get(f"{endpoint}/openai/v1/chat/completions", headers=headers, params=params)
```

## 16. Pagination
Pagination reads data in pages and follows cursors (`after`, `last_id`) until completion.

Example:
```python
if payload.get("has_more"):
    after = payload.get("last_id")
```

## 17. Endpoint validation
Checking status codes early prevents silent failures and clarifies root causes.

Example:
```python
if response.status_code != 200:
    print(response.text)
```

## 18. Preflight checks
Preflight checks validate required prerequisites before expensive operations.

Example:
```python
if not all([service_ready, endpoint_reachable, deployment_selected]):
    print("ERROR: Missing required prerequisites")
```

## 19. Runtime configuration management
Runtime settings should be defined consistently so training and evaluation runs remain reproducible.

Example:
```python
settings = {"temperature": 0.2, "max_tokens": 250, "train_ratio": 0.8}
```

## 20. Data quality filtering
Quality filters remove low-value samples (for example, too short prompts/completions).

Example:
```python
if len(completion_text) < min_completion_length:
    continue
```

## 21. Detail endpoint retrieval
A secondary endpoint can recover full message history for each completion id.

Example:
```python
url = f"{endpoint}/openai/v1/chat/completions/{completion_id}/messages"
```

## 22. 80/20 split
An 80/20 split is a common baseline for training/validation partitioning.

Example:
```python
split_index = int(len(shuffled) * 0.8)
```

## 23. Shuffle before split
Shuffling before partition avoids ordering bias and improves representativeness.

Example:
```python
random.shuffle(shuffled)
```

## 24. Deployment naming
Clear deployment names make evaluation and comparisons easier to track.

Example:
```text
support-chatbot-v1, stored-completions-distilled-v1
```

## 25. Job lifecycle states
Fine-tuning jobs move through states such as `queued`, `running`, and `succeeded`.

Example:
```text
status = "succeeded"
```

## 26. Hyperparameters
Hyperparameters influence learning behavior; in this assignment, portal defaults or selected settings are documented and justified.

Example:
```text
training_type = standard
```

## 27. Training loss
Training loss measures fit on seen data and should generally decrease during learning.

Example:
```text
training_loss ~ 0.12
```

## 28. Validation loss
Validation loss measures performance on unseen data and is critical for generalization checks.

Example:
```text
validation_loss ~ 0.34
```

## 29. Overfitting signal
A gap where validation loss stays notably above training loss indicates overfitting risk.

Example:
```text
training 0.12 vs validation 0.34 -> slight overfitting
```

## 30. Comparative testing
Comparative testing runs the same prompts against two deployments to evaluate behavioral differences.

Example:
```python
base_answer = generate_answer(BASE_DEPLOYMENT_NAME, prompt)
distilled_answer = generate_answer(DISTILLED_DEPLOYMENT_NAME, prompt)
```

## 31. Conciseness metric
Answer length can be used as a lightweight proxy for conciseness in side-by-side analysis.

Example:
```python
mean_base = comparison_df["base_len"].mean()
mean_distilled = comparison_df["distilled_len"].mean()
```

## 32. Qualitative evaluation
Beyond numeric metrics, answer quality is judged by relevance, structure, clarity, and task alignment.

Example:
```text
Check if steps are accurate, ordered, and actionable.
```

## 33. In-domain vs out-of-domain prompts
Evaluation should include prompts similar to training data and new prompts to test generalization.

Example:
```text
Dataset-like support prompts + novel troubleshooting prompts
```

## 34. Reproducible reporting
A good notebook records configuration, outputs, and interpretation so results can be audited and repeated.

Example:
```text
Include setup, metrics, comparisons, and final conclusions in one notebook.
```

## 35. Assignment takeaway
The main learning outcome is building an end-to-end loop: collect data, clean schema, train, deploy, compare models, and interpret trade-offs such as conciseness vs overfitting.
