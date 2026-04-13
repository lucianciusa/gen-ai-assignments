# 🎨 Prompt Engineering y Parametrización de Modelos

> **📖 Resumen:** Guía práctica para IAG usuario sobre técnicas de prompt engineering y explicación de parámetros de modelo (AI Foundry). Basada en guías de Microsoft y documentación de Azure Foundry.

---

## 📑 Índice

| Sección | Contenido |
|---------|-----------|
| 🎯 | **Técnicas de prompt engineering** - Explicadas con ejemplos prácticos |
| ⚙️ | **Parámetros del modelo en AI Foundry** - Configuración y uso |

---

## 🎯 Técnicas de prompt engineering

> 💡 **Nota:** Cada técnica incluye una breve explicación y un ejemplo práctico.

---

### 1️⃣ **Rol / Persona** 🎭

**📝 Explicación:** Asignar un rol claro al modelo para dirigir estilo y tono.

```markdown
💬 Ejemplo de Prompt:
"Eres un profesor de IA que explica conceptos a estudiantes principiantes. 
Explica qué es el aprendizaje supervisado en 3 puntos claros."
```

---

### 2️⃣ **Especificidad (be explicit)** 🎯

**📝 Explicación:** Ser concreto sobre formato, longitud y detalle esperado.

```markdown
💬 Ejemplo de Prompt:
"Resume en 5 viñetas (máx. 50 palabras cada una) los pasos para evaluar un modelo ML."
```

---

### 3️⃣ **Few-shot (ejemplos en prompt)** 📚

**📝 Explicación:** Proveer 1–3 ejemplos de entrada→salida para guiar el comportamiento.

```markdown
💬 Ejemplo de Prompt:
"Ejemplo: 'Traducir: Hola' → 'Hello'. 
Ahora: 'Traducir: ¿Cómo estás?' →"
```

---

### 4️⃣ **Zero-shot con instrucción clara** ⚡

**📝 Explicación:** Dar una instrucción precisa sin ejemplos; funciona para tareas directas.

```markdown
💬 Ejemplo de Prompt:
"Clasifica el siguiente texto como 'positivo', 'neutral' o 'negativo': 
'Me encantó el curso.'"
```

---

### 5️⃣ **Chain-of-thought (desglosar razonamiento)** 🔗

**📝 Explicación:** Pedir pasos intermedios para obtener respuestas más explicativas.

> ⚠️ **Advertencia:** Usar con cuidado por costos y seguridad.

```markdown
💬 Ejemplo de Prompt:
"Piensa paso a paso y explica cómo llegas a la respuesta sobre por qué X > Y. 
Luego da la conclusión final."
```

---

### 6️⃣ **Constraint / Format forcing** 🔒

**📝 Explicación:** Forzar formato de salida (JSON, tabla, lista) para parseo posterior.

```markdown
💬 Ejemplo de Prompt:
"Devuélveme la respuesta en JSON: {\"issue\":..., \"priority\":...}"
```

---

### 7️⃣ **In-context retrieval (proporcionar contexto)** 📄

**📝 Explicación:** Incluir datos relevantes (documentos, fragmentos) para respuestas precisas.

```markdown
💬 Ejemplo de Prompt:
"Basándote en el párrafo siguiente: '...texto...', 
resume los 3 puntos clave."
```

---

### 8️⃣ **Iterative refinement** 🔄

**📝 Explicación:** Generar una primera versión y pedir mejoras iterativas (claridad, concisión).

```markdown
💬 Ejemplo de Prompt:
"Escribe un resumen. Luego reescribe para que tenga tono más formal 
y 20% menos palabras."
```

---

### 9️⃣ **Prompt splitting / decomposition** 🧩

**📝 Explicación:** Dividir tareas complejas en subtareas manejables.

```markdown
💬 Ejemplo de Prompt:
"Paso 1: Identifica entidades. 
Paso 2: Extrae relaciones. 
Paso 3: Genera triples."
```

---

### 🔟 **Example-based scoring (comparar alternativas)** ⭐

**📝 Explicación:** Enviar varias respuestas candidatas y pedir que el modelo las puntúe con criterios.

```markdown
💬 Ejemplo de Prompt:
"Evalúa estas dos respuestas según claridad (0-5) y ofrece la mejor. 
Resp1: '...' Resp2: '...'"
```

---

## ⚙️ Parámetros del modelo (AI Foundry)

> 💡 **Nota:** Cada parámetro incluye explicación y ejemplo de uso en una llamada típica (JSON/HTTP) a la API.

---

### 1️⃣ **temperature** 🌡️

| Propiedad | Detalle |
|-----------|---------|
| **Descripción** | Controla la aleatoriedad en la selección de tokens |
| **Rango** | 0.0 - 2.0 (típicamente 0.0 - 1.0) |
| **Uso** | Respuestas consistentes vs. creativas |

**🔍 ¿Cómo funciona?**

La temperature modifica las probabilidades de selección de cada token:
- **temperature = 0**: El modelo siempre elige el token con mayor probabilidad → **100% determinista**
- **temperature = 0.3-0.5**: Respuestas consistentes con ligeras variaciones → **Ideal para código y datos estructurados**
- **temperature = 0.7-0.9**: Balance entre coherencia y variedad → **Conversaciones naturales**
- **temperature = 1.0+**: Alta creatividad y variabilidad → **Contenido artístico, brainstorming**

> ⚠️ **Importante:** A medida que aumenta la temperature, las probabilidades se "aplanan", dando más oportunidad a tokens menos probables.

**📊 Efecto visual:**
```
Temperature = 0.1: ████████████ (95%) █ (3%) ▏(2%)
Temperature = 0.7: ███████ (65%) ████ (25%) ██ (10%)
Temperature = 1.5: ████ (40%) ████ (30%) ███ (30%)
```

```json
// Ejemplo práctico
"temperature": 0.0  // Para generar código SQL, extracciones de datos
"temperature": 0.7  // Para asistentes conversacionales
"temperature": 1.2  // Para generar ideas creativas, nombres de productos
```

---

### 2️⃣ **top_p** (nucleus sampling) 🎲

| Propiedad | Detalle |
|-----------|---------|
| **Descripción** | Limita selección al conjunto acumulado de probabilidad top_p |
| **Rango** | 0.0 - 1.0 |
| **Uso** | Alternativa a temperature para control estadístico |

**🔍 ¿Cómo funciona?**

Top_p (nucleus sampling) selecciona tokens hasta que la suma acumulada de probabilidades alcance el valor especificado:

- **top_p = 0.1**: Solo los tokens con mayor probabilidad acumulada del 10% → **Muy conservador**
- **top_p = 0.5**: Conjunto de tokens que suman 50% de probabilidad → **Moderado**
- **top_p = 0.9**: Conjunto amplio que suma 90% de probabilidad → **Flexible pero coherente**
- **top_p = 1.0**: Considera todos los tokens posibles → **Sin restricción**

**📊 Ejemplo visual:**
```
Tokens disponibles: ["es", "fue", "era", "sería", "podría"]
Probabilidades:     [ 50%,  25%,   15%,    7%,      3% ]

top_p = 0.5  → Considera solo: ["es"] (50%)
top_p = 0.75 → Considera: ["es", "fue"] (75%)
top_p = 0.9  → Considera: ["es", "fue", "era"] (90%)
```

> 💡 **Ventaja:** A diferencia de temperature, top_p adapta dinámicamente el número de opciones según el contexto.

```json
"top_p": 0.9  // Balancea variedad y coherencia
```

---

### 3️⃣ **max_tokens** (o max_output_tokens) 📏

| Propiedad | Detalle |
|-----------|---------|
| **Descripción** | Límite de tokens en la respuesta |
| **Función** | Controla longitud máxima de salida |

```json
"max_tokens": 256
```

---

### 4️⃣ **stop** (sequences) 🛑

| Propiedad | Detalle |
|-----------|---------|
| **Descripción** | Cadenas que detienen la generación al aparecer |
| **Tipo** | Array de strings (máx. 4 secuencias típicamente) |

**🔍 ¿Cómo funciona en la práctica?**

El modelo **detiene inmediatamente** la generación cuando encuentra cualquiera de las secuencias especificadas. Las secuencias stop **NO se incluyen** en la respuesta final.

**📋 Casos de uso prácticos:**

1. **Delimitar secciones:**
```json
{
  "prompt": "Genera un resumen ejecutivo:\n",
  "stop": ["\n---", "\nConclusión:"]
}
// Se detiene antes de escribir "---" o "Conclusión:"
```

2. **Evitar contenido no deseado:**
```json
{
  "prompt": "Pregunta: ¿Cuál es la capital de Francia?\nRespuesta:",
  "stop": ["\n\nPregunta:", "\n\n"]
}
// Se detiene antes de generar otra pregunta
```

3. **Formato de diálogo:**
```json
{
  "prompt": "Usuario: Hola\nAsistente:",
  "stop": ["\nUsuario:", "\n\n"]
}
// Respuesta: "¡Hola! ¿En qué puedo ayudarte?"
// Se detiene antes de simular otro mensaje del usuario
```

4. **Estructuras de código:**
```json
{
  "prompt": "def calcular_suma(a, b):\n",
  "stop": ["\ndef ", "\nclass "]
}
// Se detiene antes de empezar otra función o clase
```

**🎯 Ejemplo completo:**

```json
// Prompt
{
  "prompt": "Escribe los 3 beneficios principales de IA:\n1.",
  "stop": ["\n\n", "\nConcluyendo"],
  "max_tokens": 200
}

// Respuesta obtenida
"1. Automatización de tareas repetitivas
2. Análisis de grandes volúmenes de datos
3. Personalización de experiencias de usuario"

// ✅ Se detuvo antes de "\n\n" (dos saltos de línea seguidos)
```

> 💡 **Tip:** Usa stop sequences para controlar exactamente dónde termina la respuesta, ahorrando tokens y evitando contenido extra.

---

### 5️⃣ **n** (num_responses) 🔢

| Propiedad | Detalle |
|-----------|---------|
| **Descripción** | Número de respuestas alternativas a generar |
| **Uso** | Una sola petición, múltiples respuestas |

```json
"n": 3
```

---

### 6️⃣ **stream** 🌊

| Propiedad | Detalle |
|-----------|---------|
| **Descripción** | Habilita recepción por chunks |
| **Uso** | Útil para UI en tiempo real |
| **Tipo** | Boolean |

```json
"stream": true
```

---

### 7️⃣ **presence_penalty** 🆕

| Propiedad | Detalle |
|-----------|---------|
| **Descripción** | Penaliza tokens que **ya han aparecido** (sin importar cuántas veces) |
| **Efecto** | Favorece diversidad de temas y vocabulario |
| **Rango** | -2.0 a 2.0 (típicamente 0.0 a 0.6) |

**🔍 ¿Cómo funciona?**

Aplica una **penalización fija** a cualquier token que ya apareció en el texto, **independientemente de las veces** que se haya repetido:

- **presence_penalty = 0**: Sin penalización → comportamiento normal
- **presence_penalty > 0**: Reduce probabilidad de tokens ya usados → **promueve explorar nuevos temas**
- **presence_penalty < 0**: Aumenta probabilidad de tokens ya usados → **refuerza temas actuales**

**📊 Efecto práctico:**

```plaintext
Texto generado: "El machine learning es importante. El machine..."

presence_penalty = 0.0  → "learning requiere datos"
presence_penalty = 0.6  → "aprendizaje automático necesita información"
// Evita repetir "machine" y "learning", usa sinónimos
```

```json
"presence_penalty": 0.3  // Moderado: algo de diversidad sin perder coherencia
"presence_penalty": 0.6  // Alto: máxima variedad de vocabulario
```

---

### 8️⃣ **frequency_penalty** 🔁

| Propiedad | Detalle |
|-----------|---------|
| **Descripción** | Penaliza tokens según **cuántas veces** han aparecido |
| **Efecto** | Reduce repeticiones literales |
| **Rango** | -2.0 a 2.0 (típicamente 0.0 a 1.0) |

**🔍 ¿Cómo funciona?**

Aplica una **penalización proporcional** basada en la **frecuencia de aparición** de cada token:

- **frequency_penalty = 0**: Sin penalización
- **frequency_penalty > 0**: Penaliza más a tokens que aparecen repetidamente → **evita repeticiones excesivas**
- **frequency_penalty < 0**: Favorece tokens frecuentes → **refuerza patrones**

**📊 Efecto práctico:**

```plaintext
Texto: "importante... importante... importante..."

frequency_penalty = 0.0  → "importante" (puede repetirse)
frequency_penalty = 0.5  → "crucial" (cambia tras 2-3 repeticiones)
frequency_penalty = 1.0  → "esencial" (evita firmemente la repetición)
```

```json
"frequency_penalty": 0.5  // Reduce repeticiones molestas
"frequency_penalty": 1.0  // Máxima variación léxica
```

---

### 🔄 **presence_penalty vs frequency_penalty** - Diferencias clave

| Aspecto | presence_penalty | frequency_penalty |
|---------|------------------|-------------------|
| **Qué cuenta** | Si el token apareció (sí/no) | **Cuántas veces** apareció |
| **Penalización** | Fija tras 1ª aparición | **Proporcional** a repeticiones |
| **Mejor para** | Diversificar **temas y vocabulario** | Evitar **repeticiones literales** |
| **Ejemplo de uso** | Artículos, exploraciones amplias | Textos descriptivos, narrativa |

**🎯 Uso combinado:**

```json
// Caso 1: Evitar repeticiones en descripciones de producto
{
  "presence_penalty": 0.0,  // Tema enfocado OK
  "frequency_penalty": 0.8  // Pero sin repetir las mismas palabras
}

// Caso 2: Brainstorming de ideas (máxima diversidad)
{
  "presence_penalty": 0.6,  // Explora diferentes ángulos
  "frequency_penalty": 0.5  // Y evita repetir conceptos
}

// Caso 3: Mantener consistencia técnica
{
  "presence_penalty": 0.0,  
  "frequency_penalty": 0.0  // Permite usar terminología técnica repetida
}
```

**📋 Ejemplo comparativo:**

```plaintext
Prompt: "Describe los beneficios del ejercicio"

Sin penalties:
"El ejercicio mejora la salud. El ejercicio aumenta la energía. 
El ejercicio fortalece el cuerpo..."

presence_penalty = 0.6:
"El ejercicio mejora la salud. La actividad física incrementa 
la vitalidad. Moverse regularmente fortalece..."
// Cambia vocabulario (ejercicio→actividad→moverse)

frequency_penalty = 0.8:
"El ejercicio mejora la salud. Mejora la energía. 
Fortalece el cuerpo..."
// Evita repetir "el ejercicio" pero mantiene tema
```

---

### 9️⃣ **temperature vs top_p** - Recomendación 🎚️

**🔍 Diferencias clave:**

| Aspecto | temperature | top_p |
|---------|-------------|-------|
| **Mecanismo** | Modifica todas las probabilidades | Filtra tokens por umbral acumulado |
| **Comportamiento** | Afecta la distribución globalmente | Adapta el conjunto de candidatos |
| **Mejor para** | Control general de creatividad | Control dinámico según contexto |

---

**📋 Guía de selección:**

| Caso de uso | Configuración recomendada |
|-------------|---------------------------|
| **Código, JSON, datos** | `temperature: 0`, `top_p: 1` |
| **Chatbots, FAQ** | `temperature: 0.7`, `top_p: 1` |
| **Contenido creativo** | `temperature: 1`, `top_p: 0.9` |
| **Máximo determinismo** | `temperature: 0`, `top_p: 1` |
---


**🎓 ¿Por qué `top_p = 1` para máximo determinismo?**

Cuando usas **`temperature = 0`**, el modelo **ya es 100% determinista** (siempre elige el token más probable).

Entonces **`top_p = 1`** significa: *"No filtres ninguna opción, deja que temperature haga todo el trabajo"*.

```plaintext
📚 Analogía:
temperature = 0  → "Siempre elige la opción #1"
top_p = 1        → "Pero puedes ver todas las opciones antes de decidir"

Es como decir: "Sé estricto (temp=0), pero sin limitarte el menú (top_p=1)"
```

---

**⚠️ ¿Por qué NO se recomienda ajustar ambos parámetros a la vez?**

Porque **ambos controlan lo mismo** (aleatoriedad vs determinismo) pero de formas diferentes, y se "pisan" entre sí:

```plaintext
🎯 Problema de ajustar ambos:

temperature = 0.2  → "Sé bastante determinista"
top_p = 0.3        → "Y además solo mira el 30% de opciones"

Resultado: ¡Doble restricción innecesaria! 
Es como poner dos cerraduras en la misma puerta.
```

**💡 Regla simple:**
- **Ajusta solo UNO** → Resultados predecibles y controlados
- **Deja el otro en valor por defecto** → `temperature = 1.0` o `top_p = 1.0`

---

**🎯 Uso combinado:**

Aunque se pueden usar ambos a la vez, **generalmente se recomienda ajustar solo uno**:

```json
// ❌ Evitar ajustar ambos agresivamente
{
  "temperature": 0.1,  
  "top_p": 0.1  // Redundante, demasiado restrictivo
}

// ✅ Recomendado: Ajustar uno, dejar el otro en valor por defecto
{
  "temperature": 0.7,
  "top_p": 1.0  // Sin filtro, solo temperature controla
}

// ✅ O viceversa
{
  "temperature": 1.0,  // Sin modificar distribución
  "top_p": 0.9  // Solo top_p controla
}

// ✅ Combinación avanzada (casos específicos)
{
  "temperature": 0.8,  // Algo de variabilidad
  "top_p": 0.95  // Pero elimina opciones muy improbables
}
```

---

### 🔟 **batch / concurrency options** 📦

| Propiedad | Detalle |
|-----------|---------|
| **Descripción** | Procesamiento de múltiples peticiones en lote |
| **Impacto** | Latencia, coste y throughput |
| **Gestión** | API/Cliente |

**🔍 ¿Para qué se usa exactamente?**

El procesamiento por **batch** permite enviar **múltiples prompts en una sola llamada API**, optimizando recursos y reduciendo latencia total.

**📋 Casos de uso prácticos:**

1. **Procesamiento masivo de documentos:**
```json
// En lugar de 100 llamadas individuales
// Enviar 1 batch con 100 documentos
{
  "model": "gpt-4",
  "requests": [
    {"prompt": "Resume documento 1: ..."},
    {"prompt": "Resume documento 2: ..."},
    // ... hasta 100
  ]
}
```

2. **Clasificación de múltiples textos:**
```json
{
  "batch": true,
  "inputs": [
    "Texto 1 para clasificar",
    "Texto 2 para clasificar",
    "Texto 3 para clasificar"
  ],
  "task": "sentiment_analysis"
}
```

3. **Generación de variantes (parámetro `n`):**
```json
// Genera 3 respuestas diferentes en una llamada
{
  "prompt": "Escribe un eslogan para producto X",
  "n": 3,  // Batch implícito: 3 generaciones
  "temperature": 0.9
}
// Respuesta: ["Eslogan A", "Eslogan B", "Eslogan C"]
```

**🎯 Beneficios del batch processing:**

| Beneficio | Detalle |
|-----------|---------|
| 💰 **Menor coste** | Descuentos por volumen en algunas APIs |
| ⚡ **Mayor throughput** | Procesa más requests por segundo |
| 🔌 **Menos overhead** | Reduce latencia de red (1 conexión vs 100) |
| 📊 **Mejor gestión** | Priorización y monitoreo centralizado |

**📊 Comparación práctica:**

```plaintext
❌ Sin batch (100 resúmenes):
  - 100 llamadas HTTP
  - Tiempo total: ~5 minutos (3s por request)
  - Coste: 100 × precio_base

✅ Con batch (100 resúmenes):
  - 1 llamada HTTP batch
  - Tiempo total: ~30 segundos
  - Coste: 80 × precio_base (20% descuento)
```

**🔧 Implementación típica:**

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

> 💡 **Tip:** Usa batch processing cuando tengas **múltiples requests independientes** (análisis de logs, clasificación de emails, generación de contenido en masa).

> ⚠️ **Limitación:** No todas las APIs soportan batch nativo. Verifica la documentación de tu proveedor (Azure AI Foundry, OpenAI, etc.).

---

## 📋 Ejemplo completo de llamada (esquema JSON)

> 🔍 **Caso de uso:** Llamada típica a AI Foundry con configuración optimizada

```json
{
  "model": "gpt-foundry-xyz",
  "input": "Eres un profesor de IA... Explica X en 3 puntos.",
  "temperature": 0.0,
  "top_p": 0.9,
  "max_tokens": 200,
  "stop": ["\n--END--"],
  "stream": false,
  "user": "iag-usuario-001"
}
```

---

## ✅ Buenas prácticas rápidas

| Caso de uso | Configuración recomendada | 🎯 |
|-------------|---------------------------|-----|
| **Instrucciones concretas y código** | `temperature: 0–0.2` + stop sequences definidas | 🎯 |
| **Creatividad** | `temperature: 0.7–1.0` o combinar con `top_p: 0.8–0.95` | 🎨 |
| **Tareas de formato específico** | Usar **few-shot** | 📋 |
| **Salida procesada automáticamente** | Forzar formato (JSON) | 🤖 |
| **Optimización** | Probar variaciones (iterative refinement) y guardar prompts exitosos como plantillas | 🔄 |

> 💡 **Tip:** Documenta los prompts que funcionan bien para reutilizarlos como plantillas.

---

## 📚 Referencias

| Fuente | Enlace |
|--------|--------|
| 🔗 **Microsoft: 15 tips to become a better prompt engineer** | [Ver artículo](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/15-tips-to-become-a-better-prompt-engineer-for-generative-ai/3882935) |
| 🔗 **Microsoft Learn: Prompt engineering concepts** | [Ver documentación](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/prompt-engineering) |

---
