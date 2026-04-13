# Practice: Prompt Engineering and Model Parameterization

This practice aims to explore prompt engineering techniques and generative AI model parameters through hands-on experimentation. It is divided into **2 independent parts**, each submitted as a separate `.ipynb` notebook.

**General objective:** Learn through experimentation how different prompting strategies and parameter settings affect model outputs, and develop judgment for applying them in real scenarios.

---

## 1) Exploring Prompt Engineering Techniques

**Objective:** Experiment with prompt engineering techniques and understand their purpose and effectiveness in different contexts.

### 1.1 - Selecting and Testing Techniques
You must **select at least 6 techniques** from those documented in `TEORIA.md` (choose the ones you find most useful or interesting). If you want to test more than 6, that is encouraged.

For each selected technique:
- **Explain** what the technique is **in your own words** (do not copy the theory definition)
- **Design a practical example** using Azure AI Foundry or the OpenAI API
- **Run the prompt** and show the model output
- **Analyze the result**: did it work as expected? what benefits did you observe? in which situations would you use this technique?

**Documentation:** Use the `TEORIA.md` file in this directory to understand each technique.

### 1.2 - Applying Techniques to Real Use Cases
After testing techniques individually, **choose 2 real use cases** (for example: technical documentation generation, sentiment analysis, structured data extraction, etc.) and apply the most appropriate techniques to each case. Justify why you chose those techniques.

### Deliverable (Part 1):
A `.ipynb` notebook including:
- **Setup section** (imports, credentials/API keys, model connection)
- **One section per technique tested** with:
  - Technique explanation (in your own words)
  - Prompt code
  - Model output
  - Critical analysis of the result
- **Real use case section** with practical application
- **Personal conclusions**: which techniques were most useful? which would you use in future projects? (optional)

---

## 2) Experimenting with Model Parameters

**Objective:** Understand how model parameters (temperature, top_p, penalties) change generated responses.

### 2.1 - Temperature Experimentation
Test the **same prompt** with different `temperature` values:
- `temperature = 0.0`
- `temperature = 0.5`
- `temperature = 1.0`
- `temperature = 1.5` (if the API supports it)

Analyze how responses change. Use a practical scenario (for example: slogan generation, code writing, technical Q&A).

### 2.2 - top_p Experimentation
Test the **same prompt** with different `top_p` values:
- `top_p = 0.1`
- `top_p = 0.5`
- `top_p = 0.9`
- `top_p = 1.0`

Keep `temperature = 1.0` to isolate the effect of `top_p`. Compare results with your temperature experiments.

### 2.3 - Penalties Experimentation
Test prompts that **tend to repeat content** (for example: product descriptions, many similar ideas) with:
- `presence_penalty = 0.0` vs `presence_penalty = 0.6`
- `frequency_penalty = 0.0` vs `frequency_penalty = 0.8`
- A combination of both penalties

Analyze what kinds of repetition each penalty helps reduce.

### 2.4 - Theory Questions (Answer in your own words)
Include a notebook section answering these questions based on your practical experience and what you learned:

1. **What is the difference between top_p and temperature?**
2. **Why is it not recommended to tune top_p and temperature at the same time?**
3. **What is the difference between presence_penalty and frequency_penalty?**

### Deliverable (Part 2):
A `.ipynb` notebook including:
- **Setup section** (imports, credentials, model)
- **One section per parameter tested** with:
  - Code showing different configurations
  - Model outputs for each configuration
  - Comparative analysis: how does each value affect behavior?
- **Theory questions section** with your reflective answers (not copied)
- **Conclusions**: which settings would you use for each type of task? (coding, creativity, data extraction, etc.)

---

## Extras

Additional work that can earn extra points:

- **Additional undocumented techniques:** Research and test prompt engineering techniques that are not listed in `TEORIA.md` but that you use regularly or discover during research (cite your sources).

- **Tutorial-style documentation:** Structure your notebook as a mini tutorial that another student could follow.

---

## Submission Format and Criteria

- **Format:** Two separate `.ipynb` notebooks (one per part), self-contained and executable.
- Minimum requirements for each notebook:
  - **Clear setup section** (imports, credentials, model used)
  - **Reproducible and documented code** with explanatory comments
  - **Visible outputs** from all runs (do not clear notebook outputs)
  - **Your own analysis and reflections** written in your own words, not copied from theory
  - **Well-structured markdown** with clear titles and sections for readability
