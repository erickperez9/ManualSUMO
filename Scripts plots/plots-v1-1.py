import argparse
import pandas as pd
import matplotlib.pyplot as plt

def graficar_datos(archivo_csv):
    # Lee el archivo CSV
    datos = pd.read_csv(archivo_csv)

    # Extrae las columnas de interés
    tripinfo_id = datos['tripinfo_id']
    tripinfo_routeLength = datos['tripinfo_routeLength']
    emissions_CO2_abs = datos['emissions_CO2_abs']
    tripinfo_duration = datos['tripinfo_duration']

    # Graficar los datos
    plt.figure(figsize=(12, 6))

    # Grafica tripinfo_routeLength versus tripinfo_id
    plt.subplot(3, 1, 1)
    plt.bar(tripinfo_id, tripinfo_routeLength, color='blue')
    plt.title('tripinfo_routeLength vs tripinfo_id')
    plt.xlabel('tripinfo_id')
    plt.ylabel('tripinfo_routeLength')
    plt.xticks(rotation=45, ha='right')  # Rotar las etiquetas del eje x para mejor visualización

    # Grafica emissions_CO2_abs versus tripinfo_id
    plt.subplot(3, 1, 2)
    plt.bar(tripinfo_id, emissions_CO2_abs, color='green')
    plt.title('emissions_CO2_abs vs tripinfo_id')
    plt.xlabel('tripinfo_id')
    plt.ylabel('emissions_CO2_abs')
    plt.xticks(rotation=45, ha='right')  # Rotar las etiquetas del eje x para mejor visualización

    # Grafica tripinfo_duration versus tripinfo_id
    plt.subplot(3, 1, 3)
    plt.bar(tripinfo_id, tripinfo_duration, color='red')
    plt.title('tripinfo_duration vs tripinfo_id')
    plt.xlabel('tripinfo_id')
    plt.ylabel('tripinfo_duration')
    plt.xticks(rotation=45, ha='right')  # Rotar las etiquetas del eje x para mejor visualización

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Configurar el parser de argumentos
    parser = argparse.ArgumentParser(description='Graficar datos desde un archivo CSV.')
    parser.add_argument('-i', '--input', type=str, help='Ruta al archivo CSV', required=True)

    # Parsear los argumentos de la línea de comandos
    args = parser.parse_args()

    # Llamar a la función para graficar los datos
    graficar_datos(args.input)
