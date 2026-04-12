# Practice: Deploying and Using Models in AI Foundry

This repository contains the practice assignment to learn how to deploy and use models in AI Foundry. The practice is divided into 3 independent parts. Each part must be submitted as a Jupyter notebook (`.ipynb`) with a clear and appropriate name.


## 1) Text, JSON, and Guardrails
Objective: Deploy a model and perform three types of interactions:
### 1.1- Generate text.
Simple text generation with a system prompt and a user prompt.

Bonus points for creating an interactive CLI chat that persists short-term memory.

[Documentation](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/generate-responses?tabs=python)
### 1.2- Generate a structured response in JSON format.
Generation of a structured response in JSON.

[Documentation](https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/structured-outputs?tabs=python-secure%2Cdotnet-entra-id&pivots=programming-language-python)
### 1.3- Implement and demonstrate Guardrails.
Create Guardrails for the model, document the process, and run tests against the model.

[Documentation](https://learn.microsoft.com/en-us/azure/foundry/guardrails/how-to-create-guardrails?tabs=python)

### Deliverable:
Notebook with code that shows the call to the model endpoint for each case, prompt examples, validation of the received JSON, and a section showing how Guardrails are configured and activated.

---

## 2) Reasoning and Function Calling
Objective: Practice with reasoning models and explore function calling

### 2.1- Reasoning
Deploy a reasoning model and parameterize different levels of reasoning (low, medium, high)

[Documentation](https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/reasoning?tabs=csharp%2Cgpt-5)

### 2.2- Function calling
Enable a web search engine to test function calls (`function calling`) that retrieve external information.

[Documentation](https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/web-search)

Bonus points for using deep research or implementing function calling with a custom function.


### Deliverable:
Notebook showing:
	- Comparative examples (same task with different reasoning levels).
	- Web search integration and a `function calling` example that combines external results with the model response.

---

## 3) Multimodal Models
### Objective:
Deploy a multimodal model and test interactions involving images, audio, and/or combined text (for example: describe an image, transcribe audio, and answer questions about its content, etc.).

[Documentation](https://learn.microsoft.com/en-us/azure/foundry-classic/foundry-models/how-to/use-chat-multi-modal?context=%2Fazure%2Ffoundry%2Fcontext%2Fcontext&pivots=programming-language-python)

### Deliverable:
Notebook with calls to the multimodal endpoint showing several examples: upload/query of images, audio, and mixed prompts; include format controls and response handling (text and/or structures).

---

Submission format and criteria
- Each part must be submitted as a self-contained `.ipynb` notebook that includes:
	- Configuration / credentials section (explaining how to configure environment variables locally).
	- Reproducible code connects to an already deployed model, performs the calls, and processes the responses.
	- Explanation cells and visible results (outputs, figures, validated JSON).
	- A final section with conclusions and issues encountered.
