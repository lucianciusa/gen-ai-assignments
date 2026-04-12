# Assignment Study Glossary - English

This glossary is written as study notes for the 01-ai-foundry-basics assignment. It explains the ideas behind the code, not just the identifiers.

## 1. Connecting to a model service
A notebook usually starts by loading configuration and building a client that can talk to the deployed model. The key idea is that the notebook does not contain the model itself; it contains the instructions and the connection details needed to reach it.

Example:
```python
load_dotenv(override=True)
client = ChatCompletionsClient(
    endpoint=FOUNDRY_ENDPOINT,
    credential=AzureKeyCredential(FOUNDRY_API_KEY),
)
```

## 2. Endpoint shape matters
An endpoint is not just a URL. In these notebooks, the shape of the endpoint determines which API flow you are using. A regular Foundry endpoint works for the first two notebooks, while the multimodal notebook needs the classic resource endpoint that ends in `/models`.

Example:
```python
classic_endpoint = FOUNDRY_MODELS_ENDPOINT.rstrip("/")
if not classic_endpoint.endswith("/models"):
    classic_endpoint += "/models"
```

## 3. Authentication with an API key
The API key is what proves the notebook is allowed to call the deployment. The pattern is simple, but it is central to every request because the client cannot send anything without valid credentials.

Example:
```python
credential = AzureKeyCredential(FOUNDRY_API_KEY)
```

## 4. Deployment name versus model name
A deployment name is the label you call from the notebook. It is not always the same thing as the model family itself. This matters because the notebook may point to a deployment that wraps a particular model version or configuration.

Example:
```python
MULTIMODAL_MODEL_DEPLOYMENT = os.getenv("MULTIMODAL_MODEL_DEPLOYMENT", "").strip()
```

## 5. Loading configuration from `.env`
The assignment keeps secrets and deployment values outside the notebook so the code is easier to share and rerun. The important habit is to read configuration at the start and fail early if something is missing.

Example:
```python
from dotenv import load_dotenv
load_dotenv(override=True)
```

## 6. Failing fast
If the notebook needs a key, an endpoint, or a deployment name, it should stop immediately when that value is missing. That is better than letting the notebook fail later in a less obvious place.

Example:
```python
missing = []
if not FOUNDRY_API_KEY:
    missing.append("FOUNDRY_API_KEY")
if missing:
    raise ValueError("Missing required environment variables: " + ", ".join(missing))
```

## 7. Chat-style prompting
The notebooks use a chat structure because it is easier to separate the system instruction from the user request. The system message sets the behavior, and the user message contains the actual task.

Example:
```python
messages = [
    SystemMessage("You are a visual analyst. Return only valid JSON."),
    UserMessage(content=[TextContentItem(text="Describe the image."), ImageContentItem(image_url=image_url)]),
]
```

## 8. Text, image, and audio as content items
A multimodal request is built from typed pieces of content. Text explains the task, image content carries the picture, and audio content carries the sound. The important idea is that the model receives structured input instead of one plain string.

Example:
```python
UserMessage(
    content=[
        TextContentItem(text="Summarize the audio."),
        AudioContentItem(input_audio=audio_input),
    ]
)
```

## 9. Modality
A modality is a type of input or output such as text, image, or audio. The assignment shows that some models can handle more than one modality, but not every combination is always supported in one single prompt.

Example:
```python
# image + text
# audio + text
# not always image + audio + text together
```

## 10. Multimodal prompts
A multimodal prompt combines more than one input type in the same request. The key study point is that the prompt must match what the model can actually process.

Example:
```python
UserMessage(
    content=[
        TextContentItem(text="Inspect the image and return JSON."),
        ImageContentItem(image_url=image_url),
    ]
)
```

## 11. Model limitations
The multimodal notebook shows an important practical lesson: capability claims are not the same as guaranteed support for every combination of inputs. If the model cannot accept image, audio, and text together, the workflow has to change.

Example:
```python
# Use separate calls when the combined prompt is not supported.
```

## 12. Split multimodal workflow
When the model cannot handle a triple-modal prompt, the safest pattern is to analyze each modality separately and then combine the results in a final text-only synthesis step.

Example:
```python
image_summary = extract_text(client.complete(messages=image_only_messages))
audio_summary = extract_text(client.complete(messages=audio_only_messages))
```

## 13. Structured output
The notebooks ask for JSON so the result can be checked programmatically. This is a good habit because it reduces ambiguity and makes the response easier to reuse.

Example:
```python
prompt = "Return only valid JSON."
```

## 14. Parsing JSON safely
Model output is not always perfectly formatted. A helper can remove code fences and parse the content, which makes the notebook more robust.

Example:
```python
def parse_json_block(text: str) -> dict:
    cleaned = text.strip()
    if cleaned.startswith("```"):
        cleaned = "\n".join(cleaned.splitlines()[1:-1])
    return json.loads(cleaned)
```

## 15. Code fences
Models sometimes wrap JSON in markdown fences. That is readable for humans, but it is inconvenient for parsing, so the notebook strips them before calling `json.loads()`.

Example:
```json
{"answer": "example"}
```

## 16. Guardrails
Guardrails are the rules that keep a model response predictable. In this assignment, they show up as instructions like “return only valid JSON” and as checks that validate the output before using it.

Example:
```python
if not value:
    raise ValueError("Missing required environment variables")
```

## 17. Validation and error handling
The notebooks do not assume success. They catch JSON parsing errors and request failures so the workflow can explain what happened instead of crashing silently.

Example:
```python
try:
    parsed = parse_json_block(text)
except json.JSONDecodeError:
    print("The response was not valid JSON.")
```

## 18. Reasoning prompts
The reasoning notebook focuses on asking the model to think through a task instead of giving a short answer immediately. The study point is how prompt wording changes the depth and structure of the answer.

Example:
```python
reasoning_task = "Plan the trip step by step and explain your choices."
```

## 19. Reasoning levels
The assignment compares different reasoning settings to see how output changes when the model is encouraged to think more or less deeply.

Example:
```python
reasoning_levels = ["low", "medium", "high"]
```

## 20. Function calling
Function calling is the pattern where the model decides it needs a tool instead of answering only in text. That is useful when the answer depends on a helper function, a lookup, or another external action.

Example:
```python
custom_tools = [
    {
        "type": "function",
        "name": "get_weather",
    }
]
```

## 21. Tool use
A tool is just a function that the model can request through the function-calling flow. The important idea is that the model is no longer working alone; it can delegate a subtask.

Example:
```python
# The model can request a tool call instead of answering directly.
```

## 22. Fallback deployment
If the preferred deployment is not available, the notebook can use another deployment as a backup. This is a practical reliability pattern, not just a convenience.

Example:
```python
selected_deployment = fallback_deployment
```

## 23. Preflight check
A preflight check is an early validation step that confirms the setup is ready before the notebook runs the main logic. It is a good way to catch configuration problems immediately.

Example:
```python
preflight_ok = True
```

## 24. Output limits
Limiting the number of tokens helps keep responses concise and controlled. This is useful when the notebook wants a short summary or a structured JSON object instead of a long answer.

Example:
```python
response = client.complete(messages=messages, temperature=0.2, max_tokens=500)
```

## 25. Prompt engineering
Prompt engineering is the practice of writing prompts that are clear enough for the model to follow. In this assignment, it means specifying the output format, the expected scope, and the kind of reasoning needed.

Example:
```python
prompt = "Inspect the image and return a JSON object with scene_summary and visible_objects."
```

## 26. Reproducibility
The multimodal notebook generates its own sample image and audio so the examples can be run again in the same way. This is important because it avoids depending on external files that may change.

Example:
```python
image_path.write_bytes(image_bytes)
audio_path.write_bytes(audio_bytes)
```

## 27. Synthetic demo data
The assignment uses synthetic image and audio examples so the notebook is deterministic and easy to test. The point is to understand the workflow, not to rely on an unpredictable real-world sample.

Example:
```python
sample = int(0.35 * 32767 * math.sin(2 * math.pi * frequency * index / sample_rate))
```

## 28. IPython display helpers
The notebook previews the generated image and audio inline so you can verify the sample data before sending it to the model.

Example:
```python
display(Image(data=image_bytes))
display(Audio(data=audio_bytes, rate=16000))
```

## 29. Binary data helpers
The assignment builds the demo image and audio from raw bytes. That is a useful reminder that notebooks can create their own test assets instead of only reading files from disk.

Example:
```python
struct.pack("<h", sample)
zlib.compress(b"".join(rows), level=9)
```

## 30. Study takeaway
The main lesson from the assignment is not only how to call a model, but how to shape the request, validate the response, and adapt the workflow when the model cannot accept every input combination.
