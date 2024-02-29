import matplotlib.pyplot as plt

# Valores de tiempos de espera
tiempo_sin_entrenar = 683697.33
tiempo_entrenado_ml = 261462.0

# Etiquetas para las barras
etiquetas = ['Sin entrenar', 'Entrenado con ML']

# Alturas de las barras
alturas = [tiempo_sin_entrenar, tiempo_entrenado_ml]

# Colores para las barras
colores = ['red', 'blue']

# Crear el gráfico de barras
plt.bar(etiquetas, alturas, color=colores)

# Añadir títulos y etiquetas
plt.ylabel('Tiempo de espera')
plt.title('Comparación de tiempos de espera entre simulaciones')
plt.ylim(0, max(alturas) * 1.2)  # Ajustar el rango del eje y para una mejor visualización

# Mostrar el gráfico
plt.show()


