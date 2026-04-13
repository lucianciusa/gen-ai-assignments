# 🎨 Prompt Engineering and Model Parameterization

> **📖 Summary:** Practical guide for the GenAI user on prompt engineering techniques and model parameter explanation (AI Foundry). Based on Microsoft guides and Azure Foundry documentation.

---

## 📑 Index

| Section | Content |
|---------|-----------|
| 🎯 | **Prompt engineering techniques** - Explained with practical examples |
| ⚙️ | **Model parameters in AI Foundry** - Configuration and usage |

---

## 🎯 Prompt engineering techniques

> 💡 **Note:** Each technique includes a brief explanation and a practical example.

---

### 1️⃣ **Role / Persona** 🎭

**📝 Explanation:** Assign a clear role to the model to guide style and tone.

```markdown
💬 Prompt Example:
"You are an AI teacher explaining concepts to beginner students.
Explain what supervised learning is in 3 clear points."
```

---

### 2️⃣ **Specificity (be explicit)** 🎯

**📝 Explanation:** Be concrete about the expected format, length, and level of detail.

```markdown
💬 Prompt Example:
"Summarize in 5 bullet points (max. 50 words each) the steps to evaluate an ML model."
```

---

### 3️⃣ **Few-shot (examples in prompt)** 📚

**📝 Explanation:** Provide 1-3 input→output examples to guide behavior.

```markdown
💬 Prompt Example:
"Example: 'Translate: Hola' → 'Hello'.
Now: 'Translate: ¿Cómo estás?' →"
```

---

### 4️⃣ **Zero-shot with a clear instruction** ⚡

**📝 Explanation:** Give a precise instruction without examples; works well for direct tasks.

```markdown
💬 Prompt Example:
"Classify the following text as 'positive', 'neutral', or 'negative':
'I loved the course.'"
```

---

### 5️⃣ **Chain-of-thought (break down reasoning)** 🔗

**📝 Explanation:** Ask for intermediate steps to get more explanatory answers.

> ⚠️ **Warning:** Use carefully due to cost and safety considerations.

```markdown
💬 Prompt Example:
"Think step by step and explain how you reach the answer for why X > Y.
Then provide the final conclusion."
```

---

### 6️⃣ **Constraint / Format forcing** 🔒

**📝 Explanation:** Force an output format (JSON, table, list) for downstream parsing.

```markdown
💬 Prompt Example:
"Return the answer in JSON: {\"issue\":..., \"priority\":...}"
```

---

### 7️⃣ **In-context retrieval (provide context)** 📄

**📝 Explanation:** Include relevant data (documents, excerpts) for accurate answers.

```markdown
💬 Prompt Example:
"Based on the following paragraph: '...text...',
summarize the 3 key points."
```

---

### 8️⃣ **Iterative refinement** 🔄

**📝 Explanation:** Generate a first draft and request iterative improvements (clarity, conciseness).

```markdown
💬 Prompt Example:
"Write a summary. Then rewrite it to have a more formal tone
and 20% fewer words."
```

---

### 9️⃣ **Prompt splitting / decomposition** 🧩

**📝 Explanation:** Split complex tasks into manageable subtasks.

```markdown
💬 Prompt Example:
"Step 1: Identify entities.
Step 2: Extract relationships.
Step 3: Generate triples."
```

---

### 🔟 **Example-based scoring (compare alternatives)** ⭐

**📝 Explanation:** Send several candidate answers and ask the model to score them against criteria.

```markdown
💬 Prompt Example:
"Evaluate these two answers for clarity (0-5) and choose the best one.
Resp1: '...' Resp2: '...'"
```

---

## ⚙️ Model parameters (AI Foundry)

> 💡 **Note:** Each parameter includes an explanation and a usage example in a typical API call (JSON/HTTP).

---

### 1️⃣ **temperature** 🌡️

| Property | Detail |
|-----------|---------|
| **Description** | Controls randomness in token selection |
| **Range** | 0.0 - 2.0 (typically 0.0 - 1.0) |
| **Use** | Consistent vs. creative responses |

**🔍 How does it work?**

Temperature modifies the selection probabilities for each token:
- **temperature = 0**: The model always chooses the highest-probability token → **100% deterministic**
- **temperature = 0.3-0.5**: Consistent responses with slight variation → **Ideal for code and structured data**
- **temperature = 0.7-0.9**: Balance between coherence and variety → **Natural conversations**
- **temperature = 1.0+**: High creativity and variability → **Artistic content, brainstorming**

> ⚠️ **Important:** As temperature increases, probabilities are "flattened," giving less likely tokens more chance.

**📊 Visual effect:**
```
Temperature = 0.1: ████████████ (95%) █ (3%) ▏(2%)
Temperature = 0.7: ███████ (65%) ████ (25%) ██ (10%)
Temperature = 1.5: ████ (40%) ████ (30%) ███ (30%)
```

```json
// Practical example
"temperature": 0.0  // For generating SQL code, data extraction
"temperature": 0.7  // For conversational assistants
"temperature": 1.2  // For generating creative ideas, product names
```

---

### 2️⃣ **top_p** (nucleus sampling) 🎲

| Property | Detail |
|-----------|---------|
| **Description** | Limits selection to the cumulative probability set top_p |
| **Range** | 0.0 - 1.0 |
| **Use** | Alternative to temperature for statistical control |

**🔍 How does it work?**

Top_p (nucleus sampling) selects tokens until the cumulative probability sum reaches the specified value:

- **top_p = 0.1**: Only tokens in the top cumulative 10% probability set → **Very conservative**
- **top_p = 0.5**: Token set that sums to 50% probability → **Moderate**
- **top_p = 0.9**: Broad set summing to 90% probability → **Flexible but coherent**
- **top_p = 1.0**: Considers all possible tokens → **No restriction**

**📊 Visual example:**
```
Available tokens: ["is", "was", "were", "would be", "could be"]
Probabilities:    [ 50%,  25%,   15%,     7%,       3% ]

top_p = 0.5  → Considers only: ["is"] (50%)
top_p = 0.75 → Considers: ["is", "was"] (75%)
top_p = 0.9  → Considers: ["is", "was", "were"] (90%)
```

> 💡 **Advantage:** Unlike temperature, top_p dynamically adapts the number of options based on context.

```json
"top_p": 0.9  // Balances variety and coherence
```

---

### 3️⃣ **max_tokens** (or max_output_tokens) 📏

| Property | Detail |
|-----------|---------|
| **Description** | Token limit in the response |
| **Function** | Controls maximum output length |

```json
"max_tokens": 256
```

---

### 4️⃣ **stop** (sequences) 🛑

| Property | Detail |
|-----------|---------|
| **Description** | Strings that stop generation when they appear |
| **Type** | Array of strings (typically up to 4 sequences) |

**🔍 How does it work in practice?**

The model **immediately stops** generation when it finds any of the specified sequences. Stop sequences are **NOT included** in the final response.

**📋 Practical use cases:**

1. **Delimit sections:**
```json
{
  "prompt": "Generate an executive summary:\n",
  "stop": ["\n---", "\nConclusion:"]
}
// Stops before writing "---" or "Conclusion:"
```

2. **Prevent unwanted content:**
```json
{
  "prompt": "Question: What is the capital of France?\nAnswer:",
  "stop": ["\n\nQuestion:", "\n\n"]
}
// Stops before generating another question
```

3. **Dialogue format:**
```json
{
  "prompt": "User: Hi\nAssistant:",
  "stop": ["\nUser:", "\n\n"]
}
// Response: "Hi! How can I help you?"
// Stops before simulating another user message
```

4. **Code structures:**
```json
{
  "prompt": "def calculate_sum(a, b):\n",
  "stop": ["\ndef ", "\nclass "]
}
// Stops before starting another function or class
```

**🎯 Complete example:**

```json
// Prompt
{
  "prompt": "Write the 3 main benefits of AI:\n1.",
  "stop": ["\n\n", "\nIn conclusion"],
  "max_tokens": 200
}

// Retrieved response
"1. Automation of repetitive tasks
2. Analysis of large volumes of data
3. Personalization of user experiences"

// ✅ Stopped before "\n\n" (two consecutive line breaks)
```

> 💡 **Tip:** Use stop sequences to control exactly where the response ends, saving tokens and avoiding extra content.

---

### 5️⃣ **n** (num_responses) 🔢

| Property | Detail |
|-----------|---------|
| **Description** | Number of alternative responses to generate |
| **Use** | One request, multiple responses |

```json
"n": 3
```

---

### 6️⃣ **stream** 🌊

| Property | Detail |
|-----------|---------|
| **Description** | Enables chunked reception |
| **Use** | Useful for real-time UI |
| **Type** | Boolean |

```json
"stream": true
```

---

### 7️⃣ **presence_penalty** 🆕

| Property | Detail |
|-----------|---------|
| **Description** | Penalizes tokens that **have already appeared** (regardless of how many times) |
| **Effect** | Favors topic and vocabulary diversity |
| **Range** | -2.0 to 2.0 (typically 0.0 to 0.6) |

**🔍 How does it work?**

Applies a **fixed penalty** to any token that has already appeared in the text, **regardless of repetition count**:

- **presence_penalty = 0**: No penalty → normal behavior
- **presence_penalty > 0**: Reduces probability of previously used tokens → **encourages exploring new topics**
- **presence_penalty < 0**: Increases probability of previously used tokens → **reinforces current topics**

**📊 Practical effect:**

```plaintext
Generated text: "Machine learning is important. Machine..."

presence_penalty = 0.0  → "learning requires data"
presence_penalty = 0.6  → "automated learning needs information"
// Avoids repeating "machine" and "learning", uses synonyms
```

```json
"presence_penalty": 0.3  // Moderate: some diversity without losing coherence
"presence_penalty": 0.6  // High: maximum vocabulary variety
```

---

### 8️⃣ **frequency_penalty** 🔁

| Property | Detail |
|-----------|---------|
| **Description** | Penalizes tokens according to **how many times** they have appeared |
| **Effect** | Reduces literal repetition |
| **Range** | -2.0 to 2.0 (typically 0.0 to 1.0) |

**🔍 How does it work?**

Applies a **proportional penalty** based on the **frequency of appearance** of each token:

- **frequency_penalty = 0**: No penalty
- **frequency_penalty > 0**: Penalizes repeatedly appearing tokens more → **avoids excessive repetition**
- **frequency_penalty < 0**: Favors frequent tokens → **reinforces patterns**

**📊 Practical effect:**

```plaintext
Text: "important... important... important..."

frequency_penalty = 0.0  → "important" (can repeat)
frequency_penalty = 0.5  → "crucial" (changes after 2-3 repetitions)
frequency_penalty = 1.0  → "essential" (firmly avoids repetition)
```

```json
"frequency_penalty": 0.5  // Reduces annoying repetitions
"frequency_penalty": 1.0  // Maximum lexical variation
```

---

### 🔄 **presence_penalty vs frequency_penalty** - Key differences

| Aspect | presence_penalty | frequency_penalty |
|---------|------------------|-------------------|
| **What it counts** | Whether the token appeared (yes/no) | **How many times** it appeared |
| **Penalty** | Fixed after first appearance | **Proportional** to repetitions |
| **Best for** | Diversifying **topics and vocabulary** | Avoiding **literal repetition** |
| **Use case example** | Articles, broad exploration | Descriptive text, narrative |

**🎯 Combined use:**

```json
// Case 1: Avoid repetition in product descriptions
{
  "presence_penalty": 0.0,  // Focused topic is OK
  "frequency_penalty": 0.8  // But without repeating the same words
}

// Case 2: Brainstorming ideas (maximum diversity)
{
  "presence_penalty": 0.6,  // Explore different angles
  "frequency_penalty": 0.5  // And avoid repeating concepts
}

// Case 3: Maintain technical consistency
{
  "presence_penalty": 0.0,
  "frequency_penalty": 0.0  // Allows repeated technical terminology
}
```

**📋 Comparative example:**

```plaintext
Prompt: "Describe the benefits of exercise"

Without penalties:
"Exercise improves health. Exercise increases energy.
Exercise strengthens the body..."

presence_penalty = 0.6:
"Exercise improves health. Physical activity increases
vitality. Moving regularly strengthens..."
// Changes vocabulary (exercise→activity→moving)

frequency_penalty = 0.8:
"Exercise improves health. Improves energy.
Strengthens the body..."
// Avoids repeating "exercise" while keeping topic
```

---

### 9️⃣ **temperature vs top_p** - Recommendation 🎚️

**🔍 Key differences:**

| Aspect | temperature | top_p |
|---------|-------------|-------|
| **Mechanism** | Modifies all probabilities | Filters tokens by cumulative threshold |
| **Behavior** | Affects distribution globally | Adapts candidate set |
| **Best for** | General creativity control | Dynamic context-based control |

---

**📋 Selection guide:**

| Use case | Recommended setting |
|-------------|---------------------------|
| **Code, JSON, data** | `temperature: 0`, `top_p: 1` |
| **Chatbots, FAQ** | `temperature: 0.7`, `top_p: 1` |
| **Creative content** | `temperature: 1`, `top_p: 0.9` |
| **Maximum determinism** | `temperature: 0`, `top_p: 1` |
---


**🎓 Why `top_p = 1` for maximum determinism?**

When you use **`temperature = 0`**, the model is **already 100% deterministic** (it always picks the most probable token).

So **`top_p = 1`** means: *"Do not filter any options; let temperature do all the work."*

```plaintext
📚 Analogy:
temperature = 0  → "Always choose option #1"
top_p = 1        → "But you can see all options before deciding"

It is like saying: "Be strict (temp=0), but do not limit your menu (top_p=1)"
```

---

**⚠️ Why is adjusting both parameters at once NOT recommended?**

Because **both control the same thing** (randomness vs determinism) in different ways, and they can interfere with each other:

```plaintext
🎯 Problem with adjusting both:

temperature = 0.2  → "Be fairly deterministic"
top_p = 0.3        → "And only look at 30% of options"

Result: Unnecessary double restriction!
It is like putting two locks on the same door.
```

**💡 Simple rule:**
- **Adjust only ONE** → Predictable, controlled results
- **Leave the other at default** → `temperature = 1.0` or `top_p = 1.0`

---

**🎯 Combined use:**

Although both can be used together, **it is generally recommended to tune only one**:

```json
// ❌ Avoid aggressively tuning both
{
  "temperature": 0.1,
  "top_p": 0.1  // Redundant, too restrictive
}

// ✅ Recommended: Tune one, leave the other at default
{
  "temperature": 0.7,
  "top_p": 1.0  // No filtering; temperature alone controls
}

// ✅ Or vice versa
{
  "temperature": 1.0,  // Do not modify distribution
  "top_p": 0.9  // Only top_p controls
}

// ✅ Advanced combination (specific cases)
{
  "temperature": 0.8,  // Some variability
  "top_p": 0.95  // But removes very unlikely options
}
```

---

### 🔟 **batch / concurrency options** 📦

| Property | Detail |
|-----------|---------|
| **Description** | Batch processing of multiple requests |
| **Impact** | Latency, cost, and throughput |
| **Management** | API/Client |

**🔍 What is it used for exactly?**

**Batch** processing allows sending **multiple prompts in a single API call**, optimizing resources and reducing total latency.

**📋 Practical use cases:**

1. **Mass document processing:**
```json
// Instead of 100 individual calls
// Send 1 batch with 100 documents
{
  "model": "gpt-4",
  "requests": [
    {"prompt": "Summarize document 1: ..."},
    {"prompt": "Summarize document 2: ..."},
    // ... up to 100
  ]
}
```

2. **Classifying multiple texts:**
```json
{
  "batch": true,
  "inputs": [
    "Text 1 to classify",
    "Text 2 to classify",
    "Text 3 to classify"
  ],
  "task": "sentiment_analysis"
}
```

3. **Generating variants (`n` parameter):**
```json
// Generates 3 different responses in one call
{
  "prompt": "Write a slogan for product X",
  "n": 3,  // Implicit batch: 3 generations
  "temperature": 0.9
}
// Response: ["Slogan A", "Slogan B", "Slogan C"]
```

**🎯 Benefits of batch processing:**

| Benefit | Detail |
|-----------|---------|
| 💰 **Lower cost** | Volume discounts in some APIs |
| ⚡ **Higher throughput** | Processes more requests per second |
| 🔌 **Less overhead** | Reduces network latency (1 connection vs 100) |
| 📊 **Better management** | Centralized prioritization and monitoring |

**📊 Practical comparison:**

```plaintext
❌ Without batch (100 summaries):
  - 100 HTTP calls
  - Total time: ~5 minutes (3s per request)
  - Cost: 100 × base_price

✅ With batch (100 summaries):
  - 1 batch HTTP call
  - Total time: ~30 seconds
  - Cost: 80 × base_price (20% discount)
```

**🔧 Typical implementation:**

```json
// Azure AI Foundry / OpenAI Batch API
{
  "custom_id": "batch-001",
  "method": "POST",
  "url": "/v1/chat/completions",
  "body": {
    "model": "gpt-4",
    "messages": [...],
    "max_tokens": 500
  }
}
```

> 💡 **Tip:** Use batch processing when you have **multiple independent requests** (log analysis, email classification, bulk content generation).

> ⚠️ **Limitation:** Not all APIs support native batch mode. Check your provider documentation (Azure AI Foundry, OpenAI, etc.).

---

## 📋 Complete call example (JSON schema)

> 🔍 **Use case:** Typical AI Foundry call with optimized configuration

```json
{
  "model": "gpt-foundry-xyz",
  "input": "You are an AI teacher... Explain X in 3 points.",
  "temperature": 0.0,
  "top_p": 0.9,
  "max_tokens": 200,
  "stop": ["\n--END--"],
  "stream": false,
  "user": "genai-user-001"
}
```

---

## ✅ Quick best practices

| Use case | Recommended setting | 🎯 |
|-------------|---------------------------|-----|
| **Concrete instructions and code** | `temperature: 0-0.2` + defined stop sequences | 🎯 |
| **Creativity** | `temperature: 0.7-1.0` or combine with `top_p: 0.8-0.95` | 🎨 |
| **Specific formatting tasks** | Use **few-shot** | 📋 |
| **Automatically processed output** | Force format (JSON) | 🤖 |
| **Optimization** | Test variations (iterative refinement) and save successful prompts as templates | 🔄 |

> 💡 **Tip:** Document prompts that work well so you can reuse them as templates.

---

## 📚 References

| Source | Link |
|--------|--------|
| 🔗 **Microsoft: 15 tips to become a better prompt engineer** | [View article](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/15-tips-to-become-a-better-prompt-engineer-for-generative-ai/3882935) |
| 🔗 **Microsoft Learn: Prompt engineering concepts** | [View documentation](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/prompt-engineering) |

---
