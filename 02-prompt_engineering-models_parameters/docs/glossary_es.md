# Glosario de estudio - Español

Estas notas explican los conceptos técnicos y las decisiones de experimentación que aparecen en la práctica 02-prompt_engineering-models_parameters.

## 1. Prompt engineering
El prompt engineering es la práctica de redactar instrucciones para que el comportamiento del modelo sea más predecible y útil. En esta práctica significa diseñar prompts con formato, alcance y nivel de detalle claros.

Ejemplo:
```python
prompt = "Extrae los 3 riesgos principales del texto y devuelve JSON válido."
```

## 2. Claridad del prompt
La claridad consiste en pedir un resultado concreto con lenguaje explícito. Un prompt claro reduce ambigüedad y baja la probabilidad de respuestas fuera de objetivo.

Ejemplo:
```python
prompt = "Resume este artículo en 4 viñetas, cada una con menos de 18 palabras."
```

## 3. Prompt con rol o persona
El prompt con rol asigna al modelo una perspectiva que ajusta tono y vocabulario. Es útil cuando el mismo contenido debe explicarse para públicos distintos.

Ejemplo:
```python
prompt = "Eres un tutor de ciencia de datos para principiantes. Explica el overfitting en lenguaje sencillo."
```

## 4. Zero-shot prompting
Zero-shot significa dar una instrucción directa sin ejemplos. Es rápido y suele bastar para tareas simples.

Ejemplo:
```python
prompt = "Clasifica el sentimiento como positivo, neutral o negativo: 'La actualización es aceptable.'"
```

## 5. Few-shot prompting
Few-shot incluye ejemplos pequeños de entrada-salida para enseñar el patrón esperado. Es útil cuando la consistencia de formato importa.

Ejemplo:
```python
prompt = """
Entrada: Hola
Salida: Hello
Entrada: Buenos días
Salida: Good morning
Entrada: Gracias
Salida:
"""
```

## 6. Especificidad en restricciones de salida
La especificidad define longitud, estructura y campos permitidos. Ayuda a evitar respuestas genéricas o demasiado largas.

Ejemplo:
```python
prompt = "Devuelve un objeto JSON con claves: title, priority, owner. Sin texto adicional."
```

## 7. Forzado de formato
El forzado de formato es pedir de forma estricta JSON, tablas, listas o salidas tipo esquema. Facilita el parseo y la validación posterior.

Ejemplo:
```python
prompt = "Responde solo como tabla markdown con columnas: Métrica | Valor | Nota."
```

## 8. Inyección de contexto
La inyección de contexto aporta texto fuente o hechos antes de la pregunta. Reduce alucinaciones porque ancla la respuesta en material conocido.

Ejemplo:
```python
prompt = f"Basándote solo en esta política:\n{policy_text}\nResponde en 3 viñetas."
```

## 9. Descomposición de tareas
La descomposición divide una petición compleja en etapas pequeñas. Suele mejorar el control y la depuración del resultado.

Ejemplo:
```python
pasos = ["extraer entidades", "encontrar relaciones", "redactar resumen final"]
```

## 10. Refinamiento iterativo
El refinamiento iterativo consiste en generar una primera versión y mejorarla con nuevas restricciones. Es útil para afinar calidad.

Ejemplo:
```python
prompt = "Reescribe la respuesta anterior con tono formal y un 20% menos de palabras."
```

## 11. Evaluación basada en ejemplos
La evaluación basada en ejemplos pide comparar alternativas con criterios explícitos. Sirve para mejorar usando rúbricas.

Ejemplo:
```python
prompt = "Puntúa la Respuesta A y B por claridad (0-5) y elige la mejor."
```

## 12. Prompt de razonamiento paso a paso
Este estilo pide pasos intermedios para resolver tareas complejas. En la práctica puede mejorar resultados difíciles, pero conviene usarlo con cuidado por coste y seguridad.

Ejemplo:
```python
prompt = "Razona las ventajas y desventajas paso a paso y luego da una recomendación final."
```

## 13. Mapeo a casos reales
Una técnica solo aporta valor si encaja con un problema real. La práctica insiste en elegir métodos por requisito de caso de uso, no por moda.

Ejemplo:
```python
caso_uso = "extracción de datos estructurados de facturas"
```

## 14. Prompting comparativo
El prompting comparativo ejecuta varias versiones del mismo prompt y contrasta salidas. Ayuda a elegir la instrucción más fiable.

Ejemplo:
```python
variantes = [prompt_a, prompt_b, prompt_c]
```

## 15. Experimentos reproducibles
La reproducibilidad exige dejar explícitos setup, entradas y parámetros para repetir resultados. Es clave para comparaciones justas.

Ejemplo:
```python
experimento = {"prompt": prompt, "temperature": 0.7, "top_p": 1.0}
```

## 16. Temperature
Temperature controla la aleatoriedad del muestreo. Valores bajos son más deterministas; valores altos aumentan variedad y creatividad.

Ejemplo:
```python
response = client.complete(messages=messages, temperature=0.2)
```

## 17. Top-p (nucleus sampling)
Top-p conserva solo el conjunto mínimo de tokens cuya probabilidad acumulada alcanza p. Es otra forma de controlar diversidad.

Ejemplo:
```python
response = client.complete(messages=messages, top_p=0.9)
```

## 18. Por qué no ajustar temperature y top_p a la vez
Cuando ambos se ajustan con fuerza al mismo tiempo, sus efectos se solapan y complican la interpretación. La práctica recomienda aislar variables.

Ejemplo:
```python
# Mantén uno fijo mientras pruebas el otro
settings = {"temperature": 1.0, "top_p": 0.5}
```

## 19. Presence penalty
Presence penalty desincentiva reutilizar tokens que ya aparecieron al menos una vez. Favorece nuevos enfoques y vocabulario.

Ejemplo:
```python
response = client.complete(messages=messages, presence_penalty=0.6)
```

## 20. Frequency penalty
Frequency penalty penaliza tokens que se repiten muchas veces. Es útil cuando la respuesta cae en repeticiones literales.

Ejemplo:
```python
response = client.complete(messages=messages, frequency_penalty=0.8)
```

## 21. Presence penalty frente a frequency penalty
Presence penalty evalúa si un token apareció; frequency penalty evalúa cuántas veces apareció. Cada uno ataca un tipo distinto de repetición.

Ejemplo:
```python
params = {"presence_penalty": 0.3, "frequency_penalty": 0.7}
```

## 22. Diseño de experimento controlado
Un diseño controlado cambia un solo factor por prueba (texto del prompt o valor de parámetro). Así las conclusiones son más fiables.

Ejemplo:
```python
baseline = {"temperature": 1.0, "top_p": 1.0}
trial = {"temperature": 0.5, "top_p": 1.0}
```

## 23. Cuadros de comparación de salidas
Un cuadro comparativo registra configuración y comportamiento observado. Convierte intuiciones en evidencia útil.

Ejemplo:
```python
filas = [{"temperature": t, "estilo": nota_estilo} for t, nota_estilo in pruebas]
```

## 24. Configuración determinista
Una configuración determinista prioriza respuestas estables, ideal para código y extracción estructurada.

Ejemplo:
```python
params = {"temperature": 0.0, "top_p": 1.0}
```

## 25. Configuración creativa
Una configuración creativa sube la variabilidad para ideación, naming o redacción narrativa.

Ejemplo:
```python
params = {"temperature": 1.1, "top_p": 0.9}
```

## 26. Max tokens
Max tokens limita la longitud de la salida. Evita verbosidad innecesaria y ayuda a controlar coste.

Ejemplo:
```python
response = client.complete(messages=messages, max_tokens=220)
```

## 27. Stop sequences
Las stop sequences son cadenas que detienen la generación antes de tiempo. Sirven para controlar límites en salidas con formato.

Ejemplo:
```python
response = client.complete(messages=messages, stop=["\n\n", "### END"])
```

## 28. Múltiples candidatas (n)
El parámetro n solicita varias alternativas en una sola llamada. Es útil para comparar respuestas candidatas rápidamente.

Ejemplo:
```python
response = client.complete(messages=messages, n=3)
```

## 29. Análisis crítico de resultados
El análisis crítico consiste en explicar qué cambió y por qué tras cada experimento. La práctica valora interpretación, no solo ejecución.

Ejemplo:
```python
nota_analisis = "Con temperature 0.0 las respuestas fueron más consistentes pero menos exploratorias."
```

## 30. Idea principal de estudio
La lección central es conectar decisiones de prompting y parámetros con objetivos concretos de tarea. Los buenos resultados nacen de experimentación deliberada, no de prueba y error al azar.
