import pandas as pd
import matplotlib.pyplot as plt
import argparse

# Configuración de los argumentos de la línea de comandos
parser = argparse.ArgumentParser(description='Graficar datos desde un archivo CSV')
parser.add_argument('-i', '--input', type=str, help='Nombre del archivo CSV de entrada', required=True)
parser.add_argument('--columna', type=str, help='Nombre de la columna a graficar', required=True)
args = parser.parse_args()

# Lee el archivo CSV
archivo_csv = args.input
datos = pd.read_csv(archivo_csv)

# Extrae las columnas de interés
tripinfo_id = datos['tripinfo_id']
columna_seleccionada = datos[args.columna]

# Graficar los datos
plt.figure(figsize=(12, 6))

# Grafica columna_seleccionada versus tripinfo_id
plt.bar(tripinfo_id, columna_seleccionada, color='blue')
plt.title(f'{args.columna} vs tripinfo_id')
plt.xlabel('tripinfo_id')
plt.ylabel(args.columna)
plt.xticks(rotation=45, ha='right')  # Rotar las etiquetas del eje x 

plt.tight_layout()
plt.show()

