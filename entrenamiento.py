import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Datos de entrenamiento (temperaturas en grados Celsius y Fahrenheit)
celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

# Definición del modelo
capa = tf.keras.layers.Dense(units=1, input_shape=[1])
modelo = tf.keras.Sequential([capa])

# Compilación del modelo
modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss='mean_squared_error'
)

# Entrenamiento del modelo
print("Comenzando entrenamiento...")
historial = modelo.fit(celsius, fahrenheit, epochs=1000, verbose=False)
print("Modelo entrenado!")

# Gráfica de la magnitud de pérdida en función del número de épocas
plt.xlabel("# Epoca")
plt.ylabel("Magnitud de perdida")
plt.plot(historial.history["loss"])  # Se grafica la magnitud de pérdida
plt.legend(["Loss"])  # Se añade la leyenda al gráfico
plt.show(block=False) # Mostrar la gráfica sin bloquear el script

# Realización de una predicción       
print("Hagamos una predicción!")
input_data = np.array([100.0]).reshape(-1,1) # Datos de entrada para la predicción

# Impresión de los datos de entrada
print("Forma de los datos de entrada:", input_data.shape)
print("Datos de entrada:", input_data)

# Realización de la predicción
resultado = modelo.predict(input_data)

# Impresión del resultado de la predicción
print("Prediction result:", resultado)

# Impresión del resultado final
print (" El resultado es", resultado , " Farenheit!")



