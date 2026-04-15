# Glosario de estudio - Español

Este glosario resume los conceptos clave aprendidos en la Práctica 3 (fine-tuning + flujo de stored completions) y los presenta como apuntes de estudio.

## 1. Fine-tuning
El fine-tuning es el proceso de adaptar un modelo base a una tarea, tono o dominio concreto usando ejemplos curados.

Ejemplo:
```python
# Entrenar un modelo especializado en soporte de Azure
```

## 2. Modelo base
El modelo base es el despliegue preentrenado original que se usa como punto de partida antes del entrenamiento personalizado.

Ejemplo:
```python
BASE_DEPLOYMENT_NAME = "gpt-4o-mini"
```

## 3. Modelo fine-tuned
Un modelo fine-tuned es el resultado entrenado que se obtiene a partir del modelo base y tu dataset.

Ejemplo:
```python
FINETUNED_DEPLOYMENT_NAME = "gpt-4o-mini-...ft-azure-support-v1"
```

## 4. Modelo destilado
En esta práctica, la destilación se usa para producir una variante especializada más compacta y compararla con el modelo base.

Ejemplo:
```python
DISTILLED_DEPLOYMENT_NAME = "gpt-4o-mini-...ft-distilled"
```

## 5. Conjunto de entrenamiento
El conjunto de entrenamiento contiene la mayoría de ejemplos y se usa para actualizar parámetros durante el fine-tuning.

Ejemplo:
```text
stored_completions_training_set.jsonl
```

## 6. Conjunto de validación
El conjunto de validación se reserva fuera del entrenamiento y sirve para estimar la capacidad de generalización.

Ejemplo:
```text
stored_completions_validation_set.jsonl
```

## 7. Formato JSONL
JSONL (JSON Lines) guarda un objeto JSON por línea. Es el formato requerido para datasets de fine-tuning conversacional.

Ejemplo:
```json
{"messages": [{"role": "system", "content": "..."}, {"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}]}
```

## 8. Esquema de mensajes en chat
Cada muestra de entrenamiento debe seguir la estructura de chat con roles y contenido textual.

Ejemplo:
```python
{"role": "user", "content": "How do I deploy a fine-tuned model?"}
```

## 9. Normalización de roles
Durante la sanitización del dataset solo deben mantenerse roles válidos (`system`, `user`, `assistant`).

Ejemplo:
```python
allowed_roles = {"system", "user", "assistant"}
```

## 10. Normalización de contenido
El contenido de mensajes puede llegar en formatos distintos y debe normalizarse a texto plano para que el entrenamiento sea compatible.

Ejemplo:
```python
content = _normalize_message_content(value)
```

## 11. Sanitización de esquema
La sanitización elimina campos inválidos y conserva únicamente lo que espera el validador de entrenamiento.

Ejemplo:
```python
cleaned.append({"role": role, "content": content})
```

## 12. Stored completions
Stored completions captura interacciones reales del modelo para transformarlas después en datasets de reentrenamiento.

Ejemplo:
```python
client.chat.completions.create(..., store=True)
```

## 13. Generación de tráfico
La generación de tráfico crea solicitudes variadas para que los logs capturados tengan suficientes ejemplos útiles.

Ejemplo:
```python
total_calls = 120
```

## 14. Etiquetado con metadata
Las etiquetas de metadata ayudan a clasificar interacciones capturadas para su filtrado y análisis.

Ejemplo:
```python
metadata={"category": "fine-tuning-assignment", "batch": "notebook-2"}
```

## 15. Extracción por REST
Los stored completions pueden extraerse mediante endpoints REST con solicitudes autenticadas.

Ejemplo:
```python
requests.get(f"{endpoint}/openai/v1/chat/completions", headers=headers, params=params)
```

## 16. Paginación
La paginación recupera datos por bloques y sigue cursores (`after`, `last_id`) hasta completar la extracción.

Ejemplo:
```python
if payload.get("has_more"):
    after = payload.get("last_id")
```

## 17. Validación de endpoint
Comprobar códigos de estado pronto evita fallos silenciosos y facilita identificar la causa raíz.

Ejemplo:
```python
if response.status_code != 200:
    print(response.text)
```

## 18. Comprobaciones previas
Las comprobaciones previas validan prerrequisitos obligatorios antes de ejecutar operaciones costosas.

Ejemplo:
```python
if not all([service_ready, endpoint_reachable, deployment_selected]):
    print("ERROR: Faltan prerrequisitos obligatorios")
```

## 19. Gestión de configuración en tiempo de ejecución
La configuración de ejecución debe definirse de forma consistente para que entrenamiento y evaluación sean reproducibles.

Ejemplo:
```python
settings = {"temperature": 0.2, "max_tokens": 250, "train_ratio": 0.8}
```

## 20. Filtrado de calidad de datos
Los filtros de calidad eliminan muestras de poco valor (por ejemplo, prompts o completions demasiado cortos).

Ejemplo:
```python
if len(completion_text) < min_completion_length:
    continue
```

## 21. Recuperación de detalle por id
Un endpoint secundario permite recuperar el historial completo de mensajes a partir del id de cada completion.

Ejemplo:
```python
url = f"{endpoint}/openai/v1/chat/completions/{completion_id}/messages"
```

## 22. División 80/20
La división 80/20 es una base habitual para particionar entrenamiento y validación.

Ejemplo:
```python
split_index = int(len(shuffled) * 0.8)
```

## 23. Mezcla antes de dividir
Mezclar los registros antes de dividir evita sesgos de orden y mejora la representatividad.

Ejemplo:
```python
random.shuffle(shuffled)
```

## 24. Nombres de deployment
Nombres de deployment claros facilitan rastrear evaluaciones y comparativas.

Ejemplo:
```text
support-chatbot-v1, stored-completions-distilled-v1
```

## 25. Estados del ciclo de vida del job
Los jobs de fine-tuning pasan por estados como `queued`, `running` y `succeeded`.

Ejemplo:
```text
status = "succeeded"
```

## 26. Hiperparámetros
Los hiperparámetros influyen en el aprendizaje; en esta práctica se documentan y justifican los valores elegidos.

Ejemplo:
```text
training_type = standard
```

## 27. Training loss
El training loss mide el ajuste sobre datos vistos y, en general, debería disminuir durante el entrenamiento.

Ejemplo:
```text
training_loss ~ 0.12
```

## 28. Validation loss
El validation loss mide rendimiento en datos no vistos y es clave para revisar la generalización.

Ejemplo:
```text
validation_loss ~ 0.34
```

## 29. Señal de sobreajuste
Una brecha donde la pérdida de validación queda claramente por encima de la de entrenamiento indica riesgo de sobreajuste.

Ejemplo:
```text
training 0.12 vs validation 0.34 -> ligero sobreajuste
```

## 30. Pruebas comparativas
Las pruebas comparativas ejecutan los mismos prompts contra dos deployments para evaluar diferencias de comportamiento.

Ejemplo:
```python
base_answer = generate_answer(BASE_DEPLOYMENT_NAME, prompt)
distilled_answer = generate_answer(DISTILLED_DEPLOYMENT_NAME, prompt)
```

## 31. Métrica de concisión
La longitud de respuesta puede usarse como métrica ligera de concisión en el análisis lado a lado.

Ejemplo:
```python
mean_base = comparison_df["base_len"].mean()
mean_distilled = comparison_df["distilled_len"].mean()
```

## 32. Evaluación cualitativa
Además de métricas numéricas, la calidad se valora por relevancia, estructura, claridad y alineación con la tarea.

Ejemplo:
```text
Comprobar si los pasos son correctos, ordenados y accionables.
```

## 33. Prompts dentro y fuera de dominio
La evaluación debe incluir prompts similares al entrenamiento y prompts nuevos para comprobar generalización.

Ejemplo:
```text
Prompts de soporte similares al dataset + prompts de resolución de incidencias nuevos
```

## 34. Reporte reproducible
Un buen notebook documenta configuración, salidas e interpretación para que los resultados sean auditables y repetibles.

Ejemplo:
```text
Incluir setup, métricas, comparativas y conclusiones finales en un único cuaderno.
```

## 35. Aprendizaje principal de la práctica
La lección central es construir un flujo extremo a extremo: capturar datos, limpiar esquema, entrenar, desplegar, comparar modelos e interpretar trade-offs como concisión frente a sobreajuste.
