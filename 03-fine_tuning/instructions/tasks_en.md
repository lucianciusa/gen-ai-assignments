# Fine-Tuning Models in Azure AI Foundry

In this practice, you will apply fine-tuning concepts for language models in Azure AI Foundry. You will train a custom model using your own dataset and evaluate performance by comparing it with the base model.

You may choose between two implementation modes:
- **Portal mode**: perform fine-tuning in Azure AI Foundry Studio (requires a process video)
- **Python SDK mode**: implement fine-tuning programmatically in Python

The practice has one integrated part, and the final deliverable is a **Jupyter Notebook** documenting the full workflow and demonstrating the fine-tuned model.

---

## Part 1) Fine-Tuned Model Training and Evaluation
**Objective:** Train a custom language model via fine-tuning, deploy it, and evaluate performance with comparative testing and metric analysis.

### 1.1 - Fine-Tuning Dataset Preparation

Create or select a custom dataset that defines the desired behavior for your fine-tuned model.

**Dataset requirements:**
- **JSONL** format compatible with Chat Completions API
- Minimum **50-100 conversation examples** (recommended: 100-300 for better results)
- Conversational role structure: `system`, `user`, `assistant`
- Split into two files:
  - `training_set.jsonl` (80% of data)
  - `validation_set.jsonl` (20% of data)

**Example use cases:**
- Technical support chatbot specialized in a specific topic
- Assistant with a specific tone/style (formal, casual, sarcastic, etc.)
- Content generator in a specific format (JSON, XML, structured markdown)
- Code assistant specialized in a language or framework
- Response system based on internal documentation

**Documentation:**
- [Preparing data for fine-tuning](https://learn.microsoft.com/es-es/azure/ai-services/openai/how-to/fine-tuning?pivots=programming-language-python#prepare-your-training-and-validation-data)
- [JSONL file format for Chat Completions](https://learn.microsoft.com/es-es/azure/ai-services/openai/how-to/fine-tuning?pivots=programming-language-python#example-file-format)

---

### 1.2 - Model Training (choose one mode)

Fine-tune an Azure OpenAI model using your prepared dataset. **Choose ONE mode:**

#### Option A - Portal Mode (Azure AI Foundry Studio)

If you choose this mode:
- Go to [Azure AI Foundry](https://ai.azure.com/)
- Navigate to **Fine-tuning** and create a new job
- Configure:
  - **Base model**: GPT-4o-mini, GPT-4o, or another available model
  - **Training type**: Standard, Global, or Developer (justify your choice)
  - **Hyperparameters**: automatic values or manually adjusted
  - **Suffix**: descriptive model name (for example: "azure-support-v1")
- Upload `training_set.jsonl` and `validation_set.jsonl`
- Monitor training progress

**Additional requirement for this mode:**
- Record a **video** showing fine-tuning job configuration
- Upload it to SharePoint and include the link in the notebook

**Documentation:**
- [Fine-tuning from Azure AI Foundry Studio](https://learn.microsoft.com/es-es/azure/foundry/openai/how-to/fine-tuning?tabs=turbo%2Cpython-secure&pivots=programming-language-studio)

#### Option B - Python SDK Mode

If you choose this mode, implement the full flow in code:

```python
from openai import AzureOpenAI
import os

# 1. Configure client
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-05-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

# 2. Upload training files
# 3. Create fine-tuning job
# 4. Monitor status and metrics
```

**Implementation requirements:**
- Code to upload training and validation files
- Fine-tuning job creation with custom configuration
- Function to monitor job state (`queued`, `running`, `succeeded`)
- Capture and visualization of training metrics
- Error handling and validation

**Documentation:**
- [Fine-tuning with Python SDK](https://learn.microsoft.com/es-es/azure/ai-services/openai/how-to/fine-tuning?pivots=programming-language-python)
- [Azure OpenAI Python SDK Reference](https://learn.microsoft.com/es-es/python/api/overview/azure/ai-openai-readme?view=azure-python-preview)

---

### 1.3 - Fine-Tuned Model Deployment

Once training is complete (`succeeded`), deploy your fine-tuned model:

**Deployment configuration:**
- **Deployment name**: descriptive name (for example: `support-chatbot-v1`)
- **Tokens per minute (TPM)**: configure based on your needs (minimum is fine for testing)

**Deployment options:**
- From the portal: Fine-tuning section -> select model -> Deploy
- With Python SDK: create deployment programmatically

Save endpoint and deployment name for testing.

**Documentation:**
- [Deploy fine-tuned models](https://learn.microsoft.com/es-es/azure/ai-services/openai/how-to/fine-tuning?pivots=programming-language-python#deploy-a-fine-tuned-model)

---

### 1.4 - Model Testing and Evaluation

Create thorough tests for your fine-tuned model and compare against the base model.

**Required tests:**

1. **Dataset-like cases**: prompts similar to training examples
2. **Out-of-dataset cases**: evaluate generalization on new cases
3. **Edge cases**: unusual or boundary scenarios
4. **Direct comparison**: same prompt to base and fine-tuned models

**Metric analysis:**

Analyze the following training metrics (portal or API):

- **`training_loss`**: loss on training data
  - Should **decrease** over epochs
  - If not decreasing: possible data or hyperparameter issues

- **`validation_loss`**: loss on validation data
  - Should decrease similarly to training loss
  - If validation loss increases while training loss decreases: **overfitting**

**Documentation:**
- [Using fine-tuned models](https://learn.microsoft.com/es-es/azure/ai-services/openai/how-to/fine-tuning?pivots=programming-language-python#use-a-fine-tuned-model)
- [Interpreting fine-tuning metrics](https://learn.microsoft.com/es-es/azure/ai-services/openai/how-to/fine-tuning?pivots=programming-language-python#analyze-your-fine-tuned-model)

---

### Deliverable:

**Required file:** One Jupyter Notebook (`.ipynb`) that includes:

#### Section 1: Introduction and Context
- **Use case description**: what problem does your fine-tuned model solve?
- **Chosen dataset**: data type and objective

#### Section 2: Fine-Tuning Process
- **If you chose Portal mode**:
  - Link to the video showing the full process

- **If you chose Python SDK mode**:
  - Complete fine-tuning code
  - Output showing training progress
  - State/error handling

Include a short explanation of chosen configuration settings.

#### Section 3: Metric Analysis
- `training_loss` and `validation_loss` values per epoch
- **Interpretation**: did the model learn correctly? Is there overfitting?
- Training-process conclusions

#### Section 4: Comparative Testing
- Base vs fine-tuned model comparisons
- Dataset-like and new cases
- **Qualitative analysis**: where did the model improve?

#### Section 5: Conclusions (optional)
- Summary of results
- Problems found and how they were resolved
- Lessons learned
- Possible future improvements

---

## Extras (Optional - Additional points)

### Extra 1: Stored Completions for Fine-Tuning with Production Data

Implement **Stored Completions** to automatically capture real production interactions and use them for continuous retraining.

Azure OpenAI can store prompts and completions in Azure Blob Storage to:
- Build fine-tuning datasets from real usage
- Improve models iteratively with production cases
- Audit and analyze model behavior

Reference:
- [Stored Completions in Azure OpenAI](https://learn.microsoft.com/en-us/azure/foundry-classic/openai/how-to/stored-completions?tabs=python-secure)

**Extra deliverable:**
- Additional notebook showing:
  - Stored completions setup (code and/or screenshots)
  - Data extraction/filtering process
  - Captured data analysis
  - Retraining results using production data
  - Before/after comparison

---

## Submission Format and Criteria

### Submission format

- **Main file**: self-contained Jupyter Notebook (`.ipynb`)
- **Allowed additional files**:
  - `training_set.jsonl` and `validation_set.jsonl` (your dataset)
  - Screenshots/illustrative images (if relevant)
  - If you chose Portal mode: video link visible in a notebook markdown cell

## Additional Resources

### Recommended official documentation

- [Complete Fine-Tuning Guide for Azure OpenAI](https://learn.microsoft.com/es-es/azure/ai-services/openai/how-to/fine-tuning)
- [Fine-Tuning Considerations](https://learn.microsoft.com/es-es/azure/foundry/concepts/fine-tuning-considerations)
- [Fine-Tuning Pricing](https://azure.microsoft.com/en-us/pricing/details/azure-openai/)
- [Fine-Tuning Best Practices](https://platform.openai.com/docs/guides/fine-tuning)

### Examples

- [Fine-Tuning Examples](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb)
