# Glosario de Estudio - Español

Este glosario resume los conceptos clave aprendidos en la Tarea 6 (redes neuronales artificiales para regresión de precios de viviendas con Keras).

## 1. Red Neuronal Artificial (RNA)
Una RNA es un modelo formado por capas de pequeñas unidades de cálculo (neuronas) que aprende parámetros a partir de los datos para mapear entradas a salidas.
Ejemplo: Una red densa con dos capas ocultas ReLU aprende a mapear las características de una propiedad a un precio continuo.

## 2. Capa densa (totalmente conectada)
Capa en la que cada neurona se conecta a todas las neuronas de la capa anterior, calculando `z = W·x + b` seguido de una activación.
Ejemplo: `layers.Dense(64, activation="relu")` aplica una transformación de 64 neuronas con ReLU.

## 3. Función de activación
Función no lineal aplicada tras la parte lineal de la neurona. Sin ella, apilar capas equivale a una sola transformación lineal.
Ejemplo: ReLU (`max(0, x)`) es la opción por defecto en capas ocultas; lineal se usa en la salida de un modelo de regresión.

## 4. ReLU
Rectified Linear Unit. Devuelve 0 para valores negativos y el propio valor para los positivos. Es eficiente y estable en la práctica para capas ocultas.

## 5. Activación lineal en la salida
En regresión, la neurona de salida no lleva activación (o `linear`) para poder producir cualquier número real, encajando con el rango ilimitado del objetivo.

## 6. Función de pérdida
Escalar que mide cuán equivocadas están las predicciones. El optimizador la minimiza durante el entrenamiento.
Ejemplo: `mse` en regresión, `binary_crossentropy` en clasificación binaria.

## 7. MSE (Error Cuadrático Medio)
Promedio de los residuos al cuadrado. Penaliza más los errores grandes, lo que va bien cuando los outliers no son extremos.

## 8. MAE (Error Absoluto Medio)
Promedio del valor absoluto de los residuos. Fácil de leer porque queda en las mismas unidades que el objetivo. Más robusto a outliers que el MSE.

## 9. RMSE (Raíz del Error Cuadrático Medio)
Raíz cuadrada del MSE. En las mismas unidades que el objetivo y útil como métrica para comunicar a stakeholders.

## 10. R² (coeficiente de determinación)
Fracción de la varianza del objetivo que el modelo es capaz de explicar. R² = 1 es perfecto; R² = 0 significa que el modelo no mejora a predecir la media.

## 11. Optimizador
Algoritmo que actualiza los pesos usando el gradiente de la pérdida.
Ejemplo: `Adam` ajusta el paso por parámetro; `SGD` con momentum es más simple pero más sensible al learning rate.

## 12. Adam
Adaptive moment estimation. Combina una media móvil de los gradientes y de sus cuadrados, con corrección de sesgo. Buen valor por defecto para prototipos.

## 13. SGD con momentum
Descenso por gradiente estocástico que conserva una fracción de la dirección de actualización anterior. Ayuda a atravesar regiones planas y gradientes ruidosos.

## 14. Learning rate (tasa de aprendizaje)
Tamaño del paso de actualización en cada iteración. Demasiado grande → divergencia; demasiado pequeño → entrenamiento lento o estancamiento.

## 15. Batch size (tamaño de lote)
Número de muestras de entrenamiento usadas por actualización de pesos. Lotes pequeños añaden ruido (regulariza); lotes grandes dan actualizaciones más estables pero menos frecuentes.

## 16. Época (epoch)
Una pasada completa por el conjunto de entrenamiento. Los modelos suelen necesitar varias épocas para converger.

## 17. Backpropagation
Algoritmo que calcula el gradiente de la pérdida respecto a cada peso aplicando la regla de la cadena desde la salida hasta la entrada.

## 18. Forward pass
Paso en el que los datos atraviesan la red para producir predicciones. Backprop reutiliza los valores intermedios cacheados.

## 19. Overfitting (sobreajuste)
El modelo aprende demasiado los datos de entrenamiento, incluido el ruido, y generaliza mal. Se detecta cuando la pérdida de validación crece mientras la de entrenamiento sigue bajando.

## 20. Underfitting (infraajuste)
El modelo es demasiado pequeño o está poco entrenado para capturar la señal. Tanto las métricas de entrenamiento como las de validación se quedan bajas.

## 21. División train / validation / test
Entrenamiento ajusta los parámetros, validación afina hiperparámetros y decide cuándo parar, test reporta el rendimiento final sin sesgo. Validación nunca debe filtrarse en el test.

## 22. Validación cruzada K-Fold
Repite la división train/validación K veces para obtener una estimación más estable. Se reporta como media ± desviación entre folds.

## 23. EarlyStopping
Callback que detiene el entrenamiento cuando la pérdida de validación deja de mejorar durante un número de épocas (`patience`) y restaura los mejores pesos.

## 24. Dropout
Desactiva aleatoriamente una fracción de las neuronas durante el entrenamiento. Funciona como regularizador al impedir que las unidades se co-adapten.

## 25. Regularización L2 (weight decay)
Añade `λ · ||w||²` a la pérdida para penalizar pesos grandes. Mantiene la red sencilla y reduce el sobreajuste.

## 26. Estandarización (z-score)
Reescala cada variable numérica a media 0 y desviación 1. Debe ajustarse solo con los datos de entrenamiento y aplicarse luego a validación y test.

## 27. One-hot encoding
Representa una variable categórica como un vector de indicadores binarios. Evita imponer un orden artificial entre categorías.

## 28. Multicolinealidad
Alta correlación entre variables de entrada. Puede desestabilizar a un modelo lineal. Es menos problemática para una red densa pequeña, pero conviene revisarla.

## 29. Residuo
Diferencia entre el valor real y la predicción. Graficar residuos vs predicciones ayuda a detectar sesgo y heterocedasticidad.

## 30. Modelo baseline
Un modelo simple (aquí, regresión lineal) que sirve como punto de referencia. Si un modelo más complejo no lo supera con claridad, la complejidad extra puede no estar justificada.

## 31. Ensemble (promediado)
Entrenar varios modelos con semillas distintas y promediar sus predicciones. Reduce varianza a costa de más cómputo.

## 32. Serialización del modelo
Guardar un modelo entrenado en un formato portable (`.keras` o `.h5`) para reutilizarlo sin volver a entrenar.

## 33. Reproducibilidad
Fijar semillas aleatorias (`numpy`, `tensorflow`, `random`) y registrar las dependencias para que volver a ejecutar el notebook devuelva los mismos números.

## 34. Asimetría (skewness)
Asimetría de una distribución. Variables objetivo de precios suelen tener cola larga a la derecha que concentra la mayor parte del error.

## 35. Perceptrón Multicapa (MLP)
Otro nombre para una red densa con propagación hacia adelante. La arquitectura de esta tarea es un MLP con dos capas ocultas.
