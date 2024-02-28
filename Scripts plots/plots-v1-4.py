import pandas as pd
import matplotlib.pyplot as plt
import argparse

# Configuración de los argumentos de la línea de comandos
parser = argparse.ArgumentParser(description='Graficar datos desde un archivo CSV')
parser.add_argument('-i', '--input', type=str, help='Nombre del archivo CSV de entrada', required=True)
parser.add_argument('--columnas', type=str, help='Nombres de las columnas a graficar separadas por coma', required=True)
args = parser.parse_args()

# Lee el archivo CSV
archivo_csv = args.input
datos = pd.read_csv(archivo_csv)

# Extrae las columnas de interés
tripinfo_id = datos['tripinfo_id']
columnas_seleccionadas = args.columnas.split(',')

# Si se elige una sola columna, graficar en una sola ventana
if len(columnas_seleccionadas) == 1:
    columna = columnas_seleccionadas[0].strip()  # Obtener el nombre de la columna
    datos_columna = datos[columna]

    # Configurar la figura y el gráfico
    plt.figure(figsize=(12, 6))

    # Graficar datos_columna versus tripinfo_id
    plt.bar(tripinfo_id, datos_columna, color='blue')
    plt.title(f'{columna} vs tripinfo_id')
    plt.xlabel('tripinfo_id')
    plt.ylabel(columna)
    plt.xticks(rotation=45)  # Rotar las etiquetas del eje x 

    plt.tight_layout()
    plt.show()
else:
    # Configura la figura y los subgráficos
    num_columnas = len(columnas_seleccionadas)
    fig, axs = plt.subplots(num_columnas, 1, figsize=(12, 6*num_columnas), sharex=True)

    # Generar una lista de colores únicos
    colores = plt.cm.tab10.colors[:num_columnas]

    # Graficar los datos en diferentes subgráficos con colores diferentes
    for i, (columna, color) in enumerate(zip(columnas_seleccionadas, colores)):
        columna = columna.strip()  # Elimina espacios en blanco al inicio y al final
        datos_columna = datos[columna]

        # Grafica datos_columna versus tripinfo_id en el subgráfico correspondiente
        axs[i].bar(tripinfo_id, datos_columna, color=color)
        axs[i].set_title(f'{columna} vs tripinfo_id')
        axs[i].set_ylabel(columna)
        axs[i].tick_params(axis='x', rotation=45)  # Rotar las etiquetas del eje x 

    # Ajustar el espacio entre los subgráficos
    plt.tight_layout()
    plt.show()

