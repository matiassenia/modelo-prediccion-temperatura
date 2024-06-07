Este repositorio contiene un pequeño proyecto de aprendizaje automático desarrollado con TensorFlow para entrenar un modelo capaz de convertir temperaturas de Celsius a Fahrenheit. Incluye el código fuente, datos de entrenamiento y documentación relevante


# Predicción de Temperaturas Fahrenheit a partir de Celsius

Este proyecto utiliza TensorFlow para construir y entrenar un modelo de aprendizaje automático que predice temperaturas en grados Fahrenheit a partir de temperaturas en grados Celsius. Utiliza un conjunto de datos de entrenamiento que consiste en pares de temperaturas en Celsius y Fahrenheit.

## Datos de Entrenamiento

Los datos de entrenamiento consisten en dos arrays NumPy: `celsius` y `fahrenheit`, que contienen temperaturas en grados Celsius y Fahrenheit respectivamente. Estos datos se utilizarán para entrenar el modelo.

## Definición del Modelo

El modelo se define utilizando TensorFlow. Consiste en una sola capa densa con una unidad y una entrada de una dimensión. Esto se implementa utilizando la clase `tf.keras.Sequential` y la capa `tf.keras.layers.Dense`.

## Compilación del Modelo

El modelo se compila utilizando el optimizador Adam con una tasa de aprendizaje de 0.1 y la función de pérdida de error cuadrático medio (`mean_squared_error`).

## Entrenamiento del Modelo

El modelo se entrena utilizando el método `fit` de TensorFlow durante 1000 épocas. El proceso de entrenamiento se realiza sin mostrar la salida en pantalla.

## Gráfica de la Pérdida

Se genera una gráfica que muestra cómo la magnitud de la pérdida cambia con el número de épocas. Esto proporciona información sobre el rendimiento del modelo durante el entrenamiento.

## Realización de Predicciones

Se realiza una predicción utilizando el modelo entrenado. Se proporciona un dato de entrada de 100.0 grados Celsius, y el modelo devuelve la predicción correspondiente en grados Fahrenheit.

## Resultado de la Predicción

El resultado de la predicción se imprime en la consola. En este caso, el modelo predice que 100.0 grados Celsius equivalen a [212.2734] grados Fahrenheit.

