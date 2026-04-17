# Glosario de estudio - Español

Este glosario resume los conceptos principales aprendidos en la Práctica 4 (embeddings, indexación vectorial y relevancia de búsqueda en Azure AI Search).

## 1. Embedding
Un embedding es una representación numérica en forma de vector que captura el significado semántico de un texto (u otro contenido).
Ejemplo: "cómo configurar búsqueda híbrida" y "configuración de recuperación híbrida" generan vectores cercanos.

## 2. Modelo de embeddings
Un modelo de embeddings transforma texto en vectores comparables por distancia o similitud.
Ejemplo: Una consulta de usuario se transforma en un vector de 1536 dimensiones antes de buscar.

## 3. Espacio vectorial
El espacio vectorial es la representación geométrica donde los elementos semánticamente parecidos quedan más cercanos.
Ejemplo: Los fragmentos sobre "ranking semántico" quedan más próximos que los de "reglas de firewall".

## 4. Similitud vectorial
La similitud vectorial es la comparación matemática entre vectores (por ejemplo, similitud coseno) para estimar cercanía semántica.
Ejemplo: una similitud coseno de 0.86 indica mayor cercanía semántica que 0.41.

## 5. Campo vectorial
Un campo vectorial es un campo del índice que guarda embeddings para búsquedas de vecinos más cercanos.
Ejemplo: `text_vector` almacena el embedding de cada chunk del documento.

## 6. Vectorizador
El vectorizador es el componente que genera vectores en indexación y/o en consulta, normalmente con embeddings de Azure OpenAI.
Ejemplo: La consulta se vectoriza automáticamente sin generar embeddings manualmente.

## 7. Búsqueda vectorial
La búsqueda vectorial recupera documentos por proximidad semántica, no por coincidencia literal de palabras.
Ejemplo: "diferencia entre vector e híbrida" puede recuperar resultados útiles aunque cambie la redacción.

## 8. k vecinos más cercanos (kNN)
kNN devuelve los k vectores más similares al vector de consulta.
Ejemplo: con `k=5`, se devuelven exactamente cinco candidatos cercanos.

## 9. Vecinos aproximados (ANN)
Los métodos ANN sacrifican una pequeña parte de exactitud para acelerar mucho la búsqueda en índices grandes.
Ejemplo: ANN puede reducir la latencia de cientos a decenas de milisegundos en corpus grandes.

## 10. HNSW
HNSW (Hierarchical Navigable Small World) es un algoritmo ANN habitual para recuperación vectorial eficiente.
Ejemplo: subir la calidad del grafo puede mejorar recall, pero también aumentar memoria y tiempo de indexación.

## 11. Esquema del índice
El esquema del índice define campos, tipos, propiedades de búsqueda y configuración de ranking/vector.
Ejemplo: `title` (texto), `chunk` (texto), `text_vector` (vector) y configuración semántica.

## 12. Configuración semántica
La configuración semántica define qué campos textuales tienen prioridad para las funciones de ranking semántico.
Ejemplo: priorizar `title` y usar `chunk` como contenido principal.

## 13. Búsqueda semántica
La búsqueda semántica mejora resultados léxicos aplicando reordenación basada en lenguaje y, opcionalmente, captions/answers.
Ejemplo: dos resultados similares por léxico pueden intercambiar posiciones tras reranking semántico.

## 14. Búsqueda híbrida
La búsqueda híbrida combina coincidencia léxica por palabras clave y similitud vectorial en una sola consulta.
Ejemplo: exigir el término exacto "vector" y, a la vez, recuperar contenido semánticamente relacionado.

## 15. Búsqueda semántica híbrida
La búsqueda semántica híbrida combina recuperación vectorial y reranking semántico para mejorar cobertura y orden final.
Ejemplo: la recuperación vectorial amplía candidatos y el reranker semántico mejora el top final.

## 16. Conjunto candidato
El conjunto candidato es el grupo inicial de documentos recuperados antes del reranking.
Ejemplo: top 50 candidatos iniciales que luego se reducen a top 5 finales.

## 17. Reranking
El reranking es el proceso de reordenar resultados iniciales con un modelo de ranking de segunda etapa.
Ejemplo: un resultado en posición 4 puede pasar a posición 1 tras reranking.

## 18. Perfil de puntuación (scoring profile)
Un perfil de puntuación es una configuración de ranking léxico que potencia campos concretos para influir en el orden final.
Ejemplo: asignar peso 5.0 a `title` y 2.0 a `chunk`.

## 19. Pesos de texto
Los pesos de texto asignan importancia relativa a campos (por ejemplo, título > cuerpo) dentro de la puntuación léxica.
Ejemplo: una coincidencia en `title` aporta más score que la misma coincidencia en `chunk`.

## 20. Perfil de puntuación por defecto
El perfil por defecto se aplica automáticamente cuando la consulta no especifica uno explícitamente.
Ejemplo: si hay perfil por defecto, el baseline puede salir impulsado sin querer.

## 21. Consulta base (baseline)
La consulta base es una ejecución neutral de referencia antes de aplicar cambios de ranking.
Ejemplo: ejecutar la query sin `scoring_profile` y luego compararla con la ejecución con perfil.

## 22. Comparación top-k
La comparación top-k revisa si los primeros k resultados cambian tras una modificación de recuperación/ranking.
Ejemplo: comparar los 5 primeros títulos antes y después de activar el perfil.

## 23. Señal de relevancia
Una señal de relevancia es cualquier indicador usado para ordenar resultados (léxico, vectorial, reranker semántico).
Ejemplo: `@search.score` y `@search.reranker_score` ayudan a interpretar por qué un resultado sube o baja.

## 24. RBAC de plano de datos
El RBAC de plano de datos controla quién puede consultar índices y documentos en Azure AI Search.
Ejemplo: `Search Index Data Reader` permite consultar, pero no modificar esquema del índice.

## 25. @search.score
`@search.score` es la puntuación principal de relevancia que devuelve Azure AI Search según el método de ranking activo.
Ejemplo: el score puede subir de 1.70 a 3.41 al aplicar boost por campos.

## 26. @search.reranker_score
`@search.reranker_score` es una puntuación adicional cuando está activo el reranking semántico.
Ejemplo: dos resultados con score léxico parecido pueden separarse por reranker score.

## 27. Razón de puntuación (con/sin perfil)
La razón de puntuación compara el score superior entre dos ejecuciones (con perfil / sin perfil) para medir el efecto del boost.
Ejemplo: razón = 3.41 / 1.70 = 2.00 (efecto de 2x).

## 28. Posición en ranking
La posición en ranking es el lugar ordinal de un resultado (1.º, 2.º, etc.) y suele ser el indicador más práctico.
Ejemplo: pasar de 4.º a 2.º suele ser más relevante que un cambio pequeño de score.

## 29. Estabilidad del ranking
La estabilidad del ranking indica que pueden cambiar los scores sin que necesariamente cambie el orden top.
Ejemplo: suben todos los scores del top-5, pero el orden se mantiene.

## 30. Precisión en k (P@k)
La precisión en k mide cuántos de los k primeros resultados son realmente relevantes.
Ejemplo: si 4 de los 5 primeros son relevantes, P@5 = 0.8.

## 31. Recall en k (R@k)
El recall en k mide cuántos resultados relevantes se recuperan dentro de los k primeros.
Ejemplo: si hay 10 relevantes totales y recuperas 4 en top-5, R@5 = 0.4.

## 32. Mean Reciprocal Rank (MRR)
MRR evalúa lo pronto que aparece el primer resultado relevante a lo largo de múltiples consultas.
Ejemplo: si el primer relevante aparece en posición 2, el recíproco es 1/2 = 0.5.

## 33. nDCG
nDCG (normalized Discounted Cumulative Gain) evalúa la calidad del ranking dando más valor a la relevancia en posiciones tempranas.
Ejemplo: un documento muy relevante en posición 1 aporta más que ese mismo documento en posición 5.

## 34. Intención de consulta
La intención de consulta es la necesidad real de información; la calidad depende de cómo el ranking se alinea con esa intención.
Ejemplo: "algoritmo de perfil vectorial" debería priorizar documentación técnica de configuración.

## 35. Recuperación para RAG
En RAG, la calidad de recuperación afecta directamente a la respuesta generada porque el modelo depende del contexto recuperado.
Ejemplo: una mala recuperación top-k suele producir respuestas incompletas o con alucinaciones.

## Ejemplos de código (fragmentos de estudio)

### A) Consulta de búsqueda vectorial
```python
from azure.search.documents.models import VectorizableTextQuery

vq = VectorizableTextQuery(
	text="diferencia entre búsqueda vectorial e híbrida",
	fields="text_vector",
	k_nearest_neighbors=5,
)

results = search_client.search(
	search_text="*",
	vector_queries=[vq],
	top=5,
)
```

### B) Consulta de búsqueda híbrida
```python
results = search_client.search(
	search_text="búsqueda híbrida",
	vector_queries=[vq],
	top=5,
)
```

### C) Consulta de búsqueda semántica
```python
from azure.search.documents.models import QueryType

results = search_client.search(
	search_text="búsqueda híbrida",
	query_type=QueryType.SEMANTIC,
	semantic_configuration_name="default-configuration",
	top=5,
)
```

### D) Creación de scoring profile (pesos de texto)
```python
from azure.search.documents.indexes.models import ScoringProfile, TextWeights

profile = ScoringProfile(
	name="boost-title-profile",
	text_weights=TextWeights(
		weights={"title": 5.0, "chunk": 2.0, "chunk_id": 1.1}
	),
)
```

### E) Comparación baseline vs perfil
```python
baseline = search_client.search(search_text=query, top=5)
with_profile = search_client.search(
	search_text=query,
	top=5,
	scoring_profile="boost-title-profile",
)
```

### F) Fragmentos de métricas
```python
# P@k
precision_at_k = relevantes_en_top_k / k

# R@k
recall_at_k = relevantes_en_top_k / relevantes_totales

# Reciprocal rank (consulta individual)
reciprocal_rank = 1 / posicion_primer_relevante

# MRR (múltiples consultas)
mrr = sum(reciprocal_ranks) / len(reciprocal_ranks)

# Razón de score (con/sin perfil)
score_ratio = top_score_con_perfil / top_score_baseline
```