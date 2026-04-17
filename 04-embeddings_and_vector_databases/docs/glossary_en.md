# Assignment Study Glossary - English

This glossary summarizes the main concepts learned in Assignment 4 (embeddings, vector indexing, and search relevance in Azure AI Search).

## 1. Embedding
An embedding is a numeric vector representation of text (or other content) that captures semantic meaning.
Example: "how to configure hybrid search" and "hybrid retrieval setup" produce vectors that are close.

## 2. Embedding model
An embedding model converts raw input text into vectors that can be compared by distance or similarity.
Example: A single user query is converted into a 1536-dimensional vector before vector search.

## 3. Vector space
A vector space is the geometric representation where semantically similar items are located closer to each other.
Example: Chunks about "semantic ranking" cluster closer than chunks about "network firewall rules".

## 4. Vector similarity
Vector similarity is the mathematical comparison between vectors (for example, cosine similarity) to estimate semantic closeness.
Example: cosine similarity 0.86 indicates higher semantic similarity than 0.41.

## 5. Vector field
A vector field is an index field that stores embedding arrays for nearest-neighbor search.
Example: `text_vector` stores the embedding for each document chunk.

## 6. Vectorizer
A vectorizer is the component that creates vectors (at indexing time and/or query time), often using Azure OpenAI embeddings.
Example: Query text is vectorized on the fly so manual embedding generation is not required.

## 7. Vector search
Vector search retrieves documents by nearest-neighbor similarity in embedding space rather than exact keyword matching.
Example: Querying "difference between vector and hybrid" can retrieve relevant text even with different wording.

## 8. k-nearest neighbors (kNN)
kNN returns the top k most similar vectors to the query vector.
Example: with `k=5`, exactly five nearest candidates are returned.

## 9. Approximate nearest neighbors (ANN)
ANN methods trade a small amount of exactness for much faster retrieval on large indexes.
Example: ANN can reduce latency from hundreds of milliseconds to tens of milliseconds on large corpora.

## 10. HNSW
HNSW (Hierarchical Navigable Small World) is a common ANN algorithm used for efficient high-dimensional vector retrieval.
Example: Increasing graph quality settings can improve recall at the cost of memory and indexing time.

## 11. Index schema
The index schema defines fields, types, searchable properties, vector settings, and ranking-related configuration.
Example: `title` (string), `chunk` (string), `text_vector` (collection of float), and semantic config.

## 12. Semantic configuration
Semantic configuration defines prioritized textual fields used by semantic ranking features.
Example: Set `title` as high priority and `chunk` as content field for semantic ranking.

## 13. Semantic search
Semantic search improves lexical results by applying language-aware reranking and optional captions/answers.
Example: Two lexical matches may swap positions after semantic reranking if one is contextually better.

## 14. Hybrid search
Hybrid search combines keyword-based lexical matching with vector similarity in a single query.
Example: A query can require the exact term "vector" while still retrieving semantically related chunks.

## 15. Semantic hybrid search
Semantic hybrid search combines vector retrieval and semantic reranking to improve both recall and final ordering quality.
Example: Vector retrieval broadens candidates; semantic reranker selects the most useful top results.

## 16. Candidate set
The candidate set is the initial group of retrieved documents before reranking steps.
Example: top 50 lexical/vector candidates are reranked to final top 5.

## 17. Reranking
Reranking is the process of reordering initially retrieved documents with a second-stage ranking model.
Example: Candidate at rank 4 can move to rank 1 after semantic reranker evaluation.

## 18. Scoring profile
A scoring profile is a lexical ranking configuration that boosts selected text fields to influence final ordering.
Example: Give `title` weight 5.0 and `chunk` weight 2.0.

## 19. Text weights
Text weights assign relative importance to fields (for example, title > body) in lexical scoring.
Example: Matching in `title` contributes more to score than the same term found only in `chunk`.

## 20. Default scoring profile
A default scoring profile applies automatically when no profile is explicitly specified in the query.
Example: If default profile is set, your baseline run may be unintentionally boosted.

## 21. Baseline query
A baseline query is a neutral run used as a reference point before applying a ranking change.
Example: Run query without `scoring_profile` argument, then compare with profile enabled.

## 22. Top-k comparison
Top-k comparison evaluates whether the first k results changed after applying a retrieval/ranking modification.
Example: Compare top 5 titles before and after enabling a scoring profile.

## 23. Relevance signal
A relevance signal is any measurable indicator used to rank documents (lexical match, vector similarity, semantic reranker output).
Example: `@search.score` + semantic reranker score together indicate ranking behavior.

## 24. Data-plane RBAC
Data-plane RBAC controls who can query indexes and documents in Azure AI Search.
Example: `Search Index Data Reader` allows querying but not index schema updates.

## 25. @search.score
`@search.score` is the primary relevance score returned by Azure AI Search for a result under the active ranking method.
Example: Score increases from 1.70 to 3.41 after enabling field boosts.

## 26. @search.reranker_score
`@search.reranker_score` is an additional score returned when semantic reranking is enabled.
Example: Two results with similar lexical score can be separated by reranker score.

## 27. Score ratio (with/without profile)
The score ratio compares top scores across two runs (with profile / without profile) to quantify boost magnitude.
Example: ratio = 3.41 / 1.70 = 2.00 (2x boost effect).

## 28. Rank position
Rank position is the ordinal location of a result (1st, 2nd, etc.) and is often the most practical relevance indicator.
Example: Moving from rank 4 to rank 2 is usually more meaningful than a small raw score change.

## 29. Ranking stability
Ranking stability means score values may change while top ordering remains similar.
Example: All top-5 scores increase but documents stay in the same rank order.

## 30. Precision at k (P@k)
Precision at k measures how many of the top k retrieved items are relevant.
Example: If 4 of top 5 are relevant, P@5 = 0.8.

## 31. Recall at k (R@k)
Recall at k measures how many relevant items are captured within the top k results.
Example: If 4 relevant docs are retrieved out of 10 total relevant docs, R@5 = 0.4.

## 32. Mean Reciprocal Rank (MRR)
MRR evaluates how early the first relevant result appears across multiple queries.
Example: First relevant at rank 2 gives reciprocal rank 1/2 = 0.5.

## 33. nDCG
nDCG (normalized Discounted Cumulative Gain) evaluates ranking quality while giving more credit to relevant items appearing earlier.
Example: A highly relevant document at rank 1 contributes more than the same document at rank 5.

## 34. Query intent
Query intent is the underlying information need; retrieval quality depends on how well ranking aligns with that intent.
Example: "vector profile algorithm" expects technical configuration docs, not general RAG overviews.

## 35. Retrieval for RAG
In RAG, retrieval quality directly affects answer quality because generation depends on the retrieved context.
Example: Weak top-k retrieval usually leads to incomplete or hallucinated answers.

## Code examples (study snippets)

### A) Vector search query
```python
from azure.search.documents.models import VectorizableTextQuery

vq = VectorizableTextQuery(
	text="difference between vector and hybrid search",
	fields="text_vector",
	k_nearest_neighbors=5,
)

results = search_client.search(
	search_text="*",
	vector_queries=[vq],
	top=5,
)
```

### B) Hybrid search query
```python
results = search_client.search(
	search_text="hybrid search",
	vector_queries=[vq],
	top=5,
)
```

### C) Semantic search query
```python
from azure.search.documents.models import QueryType

results = search_client.search(
	search_text="hybrid search",
	query_type=QueryType.SEMANTIC,
	semantic_configuration_name="default-configuration",
	top=5,
)
```

### D) Scoring profile creation (text weights)
```python
from azure.search.documents.indexes.models import ScoringProfile, TextWeights

profile = ScoringProfile(
	name="boost-title-profile",
	text_weights=TextWeights(
		weights={"title": 5.0, "chunk": 2.0, "chunk_id": 1.1}
	),
)
```

### E) Baseline vs profile comparison
```python
baseline = search_client.search(search_text=query, top=5)
with_profile = search_client.search(
	search_text=query,
	top=5,
	scoring_profile="boost-title-profile",
)
```

### F) Metric snippets
```python
# P@k
precision_at_k = relevant_in_top_k / k

# R@k
recall_at_k = relevant_in_top_k / total_relevant

# Reciprocal rank (single query)
reciprocal_rank = 1 / first_relevant_rank

# MRR (multiple queries)
mrr = sum(reciprocal_ranks) / len(reciprocal_ranks)

# Score ratio (with/without profile)
score_ratio = top_score_with_profile / top_score_baseline
```