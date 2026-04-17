# gen-ai-assignments

Repository for all Generative AI assignments, supporting materials, and study notes.

## Structure

Each assignment lives in its own folder and may include notebooks, helper scripts, assets, and documentation.

1. Azure AI Foundry fundamentals: guardrails, reasoning + function calling, and multimodal basics.
- `01-foundry_exploration/`
  - `*.ipynb`
  - `*.py`
  - `assets/`
  - `images/`
  - `docs/`
  - `instructions/`


2. Prompt design techniques and controlled experiments with model parameters.
- `02-prompt_engineering-models_parameters/`
  - `*.ipynb`
  - `assets/`
  - `images/`
  - `docs/`
  - `instructions/`

3. End-to-end fine-tuning workflow, including stored completions and base-vs-distilled evaluation.
- `03-fine_tuning/`
  - `*.ipynb`
  - `assets/`
  - `data/`
  - `images/`
  - `docs/`
  - `instructions/`
  - `outputs/`

4. Embeddings and vector databases in Azure AI Search: indexing pipeline, vector/hybrid/semantic retrieval, and scoring-profile relevance tuning.
- `04-embeddings_and_vector_databases/`
  - `01_import_data_wizard.ipynb`
  - `02_vector_search.ipynb`
  - `03_extra_option_b_scoring_profile.ipynb`
  - `assets/`
  - `images/`
  - `docs/`
    - `glossary_en.md`
    - `glossary_es.md`
    - `container_docs/`
  - `instructions/`

## Organization Notes

- Keep notebook-specific materials inside the corresponding assignment folder.
- Use `docs/` for glossary files, notes, or supporting explanations.
- Use `assets/` and `images/` for generated or referenced media.
- Use `instructions/` for prompts, task descriptions, or assignment guidance.

## Quick start

1. Create and activate a Python environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy the relevant `.env.example` file from the assignment folder you are working in and set your values.
4. Open the notebooks in that assignment folder and run the exercises.
