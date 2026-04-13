# Glosario de estudio - Español

Estas notas explican los conceptos técnicos y las técnicas que aparecen en la práctica 01-ai-foundry-basics.

## 1. Conectar con un servicio de modelo
Un cuaderno no contiene el modelo en sí: contiene la configuración y el cliente que permiten llamarlo. La idea principal es preparar el entorno y construir la conexión correcta antes de enviar cualquier solicitud.

Ejemplo:
```python
load_dotenv(override=True)
client = ChatCompletionsClient(
    endpoint=FOUNDRY_ENDPOINT,
    credential=AzureKeyCredential(FOUNDRY_API_KEY),
)
```

## 2. La forma del endpoint importa
El endpoint no es solo una URL. Según su forma, el cuaderno usa un flujo distinto. En esta práctica, un endpoint normal de Foundry sirve para los dos primeros cuadernos, mientras que el cuaderno multimodal necesita el endpoint clásico del recurso que termina en `/models`.

Ejemplo:
```python
classic_endpoint = FOUNDRY_MODELS_ENDPOINT.rstrip("/")
if not classic_endpoint.endswith("/models"):
    classic_endpoint += "/models"
```

## 3. Autenticación con clave de API
La clave de API es lo que permite que el notebook se autentique frente al servicio. Sin una credencial válida, el cliente no puede enviar solicitudes.

Ejemplo:
```python
credential = AzureKeyCredential(FOUNDRY_API_KEY)
```

## 4. Despliegue frente a modelo
El nombre del despliegue es la etiqueta que usas desde el cuaderno. No siempre coincide con el nombre comercial del modelo; puede incluir una versión o una configuración concreta.

Ejemplo:
```python
MULTIMODAL_MODEL_DEPLOYMENT = os.getenv("MULTIMODAL_MODEL_DEPLOYMENT", "").strip()
```

## 5. Cargar configuración desde `.env`
La práctica guarda secretos y valores de despliegue fuera del cuaderno para que el código sea más fácil de reutilizar. La práctica correcta es leer la configuración al principio y detenerse si falta algo importante.

Ejemplo:
```python
from dotenv import load_dotenv
load_dotenv(override=True)
```

## 6. Fallar pronto
Si faltan una clave, un endpoint o un despliegue, es mejor detener el cuaderno de inmediato que dejar que falle más adelante de forma confusa.

Ejemplo:
```python
missing = []
if not FOUNDRY_API_KEY:
    missing.append("FOUNDRY_API_KEY")
if missing:
    raise ValueError("Missing required environment variables: " + ", ".join(missing))
```

## 7. Prompts en formato chat
Los cuadernos usan una estructura de mensajes porque separa bien la instrucción del sistema y la tarea del usuario. El mensaje del sistema define el comportamiento y el del usuario contiene la petición real.

Ejemplo:
```python
messages = [
    SystemMessage("You are a visual analyst. Return only valid JSON."),
    UserMessage(content=[TextContentItem(text="Describe the image."),
    ImageContentItem(image_url=image_url)]),
]
```

## 8. Texto, imagen y audio como elementos de contenido
Una solicitud multimodal se construye con partes tipadas de contenido. El texto explica la tarea, la imagen lleva la foto y el audio lleva el sonido.

Ejemplo:
```python
UserMessage(
    content=[
        TextContentItem(text="Summarize the audio."),
        AudioContentItem(input_audio=audio_input),
    ]
)
```

## 9. Modalidad
Una modalidad es un tipo de entrada o salida, como texto, imagen o audio. La práctica muestra que algunos modelos aceptan más de una modalidad, pero no todas las combinaciones están garantizadas en un solo prompt.

Ejemplo:
```python
# imagen + texto
# audio + texto
# no siempre imagen + audio + texto juntos
```

## 10. Prompts multimodales
Un prompt multimodal combina más de un tipo de entrada en la misma solicitud. La lección importante es que el prompt debe coincidir con lo que el modelo puede procesar realmente.

Ejemplo:
```python
UserMessage(
    content=[
        TextContentItem(text="Inspect the image and return JSON."),
        ImageContentItem(image_url=image_url),
    ]
)
```

## 11. Limitaciones del modelo
El cuaderno multimodal deja una lección práctica muy clara: que un modelo sea multimodal no significa que acepte cualquier combinación de entradas en una sola llamada. Si no soporta imagen, audio y texto juntos, el flujo debe adaptarse.

Ejemplo:
```python
# Usa llamadas separadas cuando el prompt combinado no esté soportado.
```

## 12. Flujo multimodal dividido
Cuando el modelo no puede procesar las tres modalidades juntas, la forma más segura es analizar cada modalidad por separado y luego combinar los resultados en una síntesis final solo de texto.

Ejemplo:
```python
image_summary = extract_text(client.complete(messages=image_only_messages))
audio_summary = extract_text(client.complete(messages=audio_only_messages))
```

## 13. Salida estructurada
Los cuadernos piden JSON para que la respuesta se pueda comprobar de forma automática. Es una buena práctica porque reduce la ambigüedad y facilita reutilizar la salida.

Ejemplo:
```python
prompt = "Return only valid JSON."
```

## 14. Analizar JSON con seguridad
La salida del modelo no siempre llega perfectamente formateada. Un helper puede quitar los fences de Markdown y analizar el contenido, lo que hace el cuaderno más robusto.

Ejemplo:
```python
def parse_json_block(text: str) -> dict:
    cleaned = text.strip()
    if cleaned.startswith("```"):
        cleaned = "\n".join(cleaned.splitlines()[1:-1])
    return json.loads(cleaned)
```

## 15. Fences de Markdown
A veces el modelo envuelve el JSON en bloques de Markdown. Eso es legible para una persona, pero incómodo para analizarlo automáticamente.

Ejemplo:
```json
{"answer": "example"}
```

## 16. Guardrails
Los guardrails son las reglas que mantienen la salida del modelo dentro de un formato predecible. En esta práctica aparecen como instrucciones del tipo “devuelve solo JSON válido” y como validaciones previas.

Ejemplo:
```python
if not value:
    raise ValueError("Missing required environment variables")
```

## 17. Validación y manejo de errores
Los cuadernos no asumen que todo saldrá bien. Capturan errores de parseo o de solicitud para explicar qué ocurrió en vez de fallar en silencio.

Ejemplo:
```python
try:
    parsed = parse_json_block(text)
except json.JSONDecodeError:
    print("La respuesta no era JSON válido.")
```

## 18. Prompts de razonamiento
El cuaderno de razonamiento se centra en pedir al modelo que piense paso a paso en lugar de dar una respuesta breve inmediata. La idea de estudio es ver cómo cambia la respuesta según la forma del prompt.

Ejemplo:
```python
reasoning_task = "Plan the trip step by step and explain your choices."
```

## 19. Niveles de razonamiento
La práctica compara distintos niveles de razonamiento para observar cómo cambia la profundidad de la respuesta.

Ejemplo:
```python
reasoning_levels = ["low", "medium", "high"]
```

## 20. Function calling
Function calling es el patrón en el que el modelo decide que necesita una herramienta en lugar de responder solo en texto. Es útil cuando la respuesta depende de una función, una consulta o una acción externa.

Ejemplo:
```python
custom_tools = [
    {
        "type": "function",
        "name": "get_weather",
    }
]
```

## 21. Uso de herramientas
Una herramienta es simplemente una función que el modelo puede pedir durante el flujo de function calling. La idea importante es que el modelo deja de trabajar solo y delega una parte de la tarea.

Ejemplo:
```python
# El modelo puede solicitar una llamada a herramienta en lugar de responder directamente.
```

## 22. Despliegue de respaldo
Si el despliegue preferido no está disponible, el cuaderno puede usar otro como respaldo. Es una técnica de fiabilidad, no solo una comodidad.

Ejemplo:
```python
selected_deployment = fallback_deployment
```

## 23. Comprobación previa
Una comprobación previa valida que la configuración esté lista antes de ejecutar la lógica principal. Es una forma sencilla de detectar problemas de configuración al principio.

Ejemplo:
```python
preflight_ok = True
```

## 24. Límites de salida
Limitar el número de tokens ayuda a mantener la respuesta breve y controlada. Esto es útil cuando el cuaderno quiere un resumen corto o un JSON estructurado.

Ejemplo:
```python
response = client.complete(messages=messages, temperature=0.2, max_tokens=500)
```

## 25. Prompt engineering
Prompt engineering es la práctica de escribir instrucciones claras para que el modelo siga exactamente lo que necesitas. En esta práctica significa pedir formato, alcance y tipo de respuesta con precisión.

Ejemplo:
```python
prompt = "Inspect the image and return a JSON object with scene_summary and visible_objects."
```

## 26. Reproducibilidad
El cuaderno multimodal genera su propia imagen y su propio audio de ejemplo para que puedas repetir el ejercicio siempre del mismo modo. Así no dependes de archivos externos que cambien.

Ejemplo:
```python
image_path.write_bytes(image_bytes)
audio_path.write_bytes(audio_bytes)
```

## 27. Datos sintéticos de demostración
La práctica usa ejemplos sintéticos de imagen y audio para que el cuaderno sea determinista y fácil de probar. La meta es entender el flujo, no depender de un ejemplo real impredecible.

Ejemplo:
```python
sample = int(0.35 * 32767 * math.sin(2 * math.pi * frequency * index / sample_rate))
```

## 28. Ayudas de visualización de IPython
El cuaderno muestra la imagen y el audio generados dentro de la propia notebook para verificar el material antes de enviarlo al modelo.

Ejemplo:
```python
display(Image(data=image_bytes))
display(Audio(data=audio_bytes, rate=16000))
```

## 29. Ayudas para datos binarios
La práctica construye la imagen y el audio de demostración a partir de bytes crudos. Eso recuerda que un cuaderno también puede crear sus propios archivos de prueba.

Ejemplo:
```python
struct.pack("<h", sample)
zlib.compress(b"".join(rows), level=9)
```

## 30. Idea principal de estudio
La lección central no es solo cómo llamar a un modelo, sino cómo formular la petición, validar la respuesta y adaptar el flujo cuando el modelo no acepta todas las combinaciones de entrada.
