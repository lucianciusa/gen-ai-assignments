# PRACTICE: Embeddings and Vector Database (Azure AI Search)

> Format: MD. Submit in the topic folder. This practice has two parts: wizard documentation (Import data) and executing searches.

---

## Summary

Objective: Build and document an indexing pipeline using the Azure portal "Import data" wizard (integrated vectorization). Then run searches against the created index: Vector Search, Hybrid Search, Semantic Search, and Semantic Hybrid Search. Include screenshots, explanations, and results.

---

## Prerequisites

- Azure account with an Azure AI Search resource (Basic or higher recommended).
- Azure Blob Storage container with documents (PDF/DOCX/HTML).
- Azure OpenAI resource with an embeddings deployment.

---

## PART 1 - Create the index with the wizard (Import data)

This part is documentation-oriented: follow the portal wizard to create the index. Submit screenshots and explanations in this file.

Portal steps:
1. In **Azure AI Search**, select **Import data**.
2. Choose scenario: **RAG** (not agentic retrieval).
3. Connect to **Azure Blob Storage** (select the document container). Authenticate using Managed Identity or key.
4. In vectorization, choose provider (Azure OpenAI / Foundry) and embeddings deployment.
5. Review schema inference and adjust fields if needed.
6. Finish: the wizard creates Data Source, Index, Skillset (if enrichment is enabled), Indexer, and optional Knowledge Store.

### Required screenshots and explanations

- **INDEX (Index schema):** capture the created index definition.
- **SEMANTIC CONFIGURATION:** screenshot of semantic configuration. Explain what it is and how it is configured.
- **VECTOR PROFILE:** screenshot of `Algorithm` and `Vectorizer` sections in the index. Explain each and how they are configured.
- **SKILLSET:** screenshot of the wizard-generated skillset. Explain what it is and the steps it includes.

---

## PART 2 - Practical searches (Python execution)

Submit a script or notebook (`.ipynb` recommended) executing the following search types and top-5 result examples:

1. Vector Search
2. Hybrid Search (vector + keyword)
3. Semantic Search (`query_type=semantic`)
4. Semantic Hybrid Search (semantic + vector)

[Semantic ranking reference](https://github.com/Azure-Samples/azure-search-python-samples/blob/main/Quickstart-Semantic-Ranking/semantic-ranking-quickstart.ipynb)
[Vector search reference](https://github.com/Azure-Samples/azure-search-python-samples/blob/main/Quickstart-Vector-Search/vector-search-quickstart.ipynb)

## Extra (choose at least ONE option and document it)

A. Add a **custom skill** (OCR or custom endpoint) to the skillset: document implementation and indexing impact. Reference: https://learn.microsoft.com/en-us/azure/search/cognitive-search-defining-skillset

B. Add a **scoring profile** to the index and explain ranking impact. Reference: https://learn.microsoft.com/es-es/azure/search/index-add-scoring-profiles?tabs=python

C. Implement **multimodal search** (text + images) if documents contain images. Reference: https://learn.microsoft.com/en-us/azure/search/multimodal-search-overview

---

## Deliverables

1. A `.docx`, `.ipynb`, or `.md` file documenting Part 1.
2. `practica_vector_search.ipynb` or `practica_vector_search.py` with Part 2 executed and results included.
3. (Optional) Documentation of the selected extra implementation.

---
