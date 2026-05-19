# Glosario — Redes Neuronales Convolucionales (CNN)

| Término | Definición |
|---------|-----------|
| **Capa convolucional** | Capa que aplica filtros (kernels) aprendibles a partes locales de la entrada, compartiendo pesos en todas las posiciones espaciales para detectar patrones como bordes y trazos. |
| **Kernel / Filtro** | Pequeña matriz de pesos (ej. 3×3) que se desliza sobre la entrada para producir un mapa de características. Cada filtro aprende a detectar un patrón específico. |
| **Mapa de características** | Salida de una capa convolucional — una cuadrícula 2D de activaciones que muestra dónde un filtro respondió con mayor intensidad. |
| **Relleno (Padding)** | Agregar ceros alrededor del borde de la entrada (`same` padding) para que el mapa de características de salida tenga las mismas dimensiones espaciales que la entrada. |
| **Stride** | Tamaño del paso del filtro al deslizarse sobre la entrada. Stride > 1 reduce las dimensiones espaciales. |
| **Pooling** | Operación de reducción dimensional. `MaxPooling` conserva la activación más alta en cada parche; reduce el cómputo y añade invariancia a traslaciones. |
| **Flatten** | Transforma un mapa de características 3D (alto × ancho × canales) en un vector 1D para el clasificador completamente conectado. |
| **Normalización por lotes (Batch Normalization)** | Normaliza las activaciones a lo largo de un mini-lote durante el entrenamiento, acelerando la convergencia y reduciendo la sensibilidad a la tasa de aprendizaje. |
| **Dropout** | Técnica de regularización: desactiva aleatoriamente una fracción de neuronas durante el entrenamiento para prevenir la co-adaptación y el sobreajuste. |
| **Softmax** | Función de activación en la capa de salida que convierte puntuaciones brutas (logits) en una distribución de probabilidad sobre las clases. |
| **Entropía cruzada categórica dispersa** | Función de pérdida para clasificación multiclase cuando las etiquetas se proporcionan como enteros (no como vectores one-hot). |
| **Early Stopping** | Callback que detiene el entrenamiento cuando una métrica monitorizada (ej. `val_loss`) deja de mejorar, restaurando los mejores pesos encontrados. |
| **ReduceLROnPlateau** | Callback que reduce la tasa de aprendizaje por un factor cuando la métrica monitorizada se estanca, ayudando a escapar de mínimos locales. |
| **Aumento de datos (Data Augmentation)** | Aplicar transformaciones aleatorias (rotación, desplazamiento, zoom) a imágenes de entrenamiento en tiempo de ejecución para aumentar artificialmente la diversidad del conjunto de datos. |
| **MNIST** | Modified National Institute of Standards and Technology — 70 000 imágenes en escala de grises de 28×28 píxeles de dígitos manuscritos 0–9 con etiquetas. |
| **Matriz de confusión** | Tabla N×N que compara etiquetas reales (filas) frente a predicciones (columnas); la diagonal representa predicciones correctas. |
| **ImageDataGenerator** | Utilidad de Keras que genera mini-lotes aumentados en tiempo real sin ampliar el conjunto de datos en disco. |
| **Inferencia** | Ejecutar un modelo entrenado sobre nuevas entradas para producir predicciones, sin actualizar pesos. |
| **Aprendizaje por transferencia** | Reutilizar pesos de un modelo entrenado en una tarea (ej. ImageNet) como punto de partida para una tarea relacionada. |
| **Campo receptivo** | Región de la entrada original que influye en la activación de una neurona particular; crece con la profundidad de la red. |
