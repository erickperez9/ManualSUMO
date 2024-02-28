import traci
import csv
import time
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Iniciar la conexión con SUMO
traci.start(["sumo", "-c", "/home/sumo/sumo/tools/2024-02-05-16-21-35/osm.sumocfg"])

# Archivo de salida
csv_file_path = 'datos_simulacion_co2.csv'

with open(csv_file_path, 'w', newline='') as csvfile:
    
    csv_writer = csv.writer(csvfile)

    # Cabecera del CSV
    csv_writer.writerow(['Time', 'VehicleID', 'CO2'])

    # Ejecutar la simulación 
    while traci.simulation.getMinExpectedNumber() > 0:
        current_time = traci.simulation.getCurrentTime() / 1000  # Convertir a segundos

        for veh_id in traci.vehicle.getIDList():
            co2 = traci.vehicle.getCO2Emission(veh_id)         
            print(f"Tiempo: {current_time}, ID del Vehículo: {veh_id}, CO2: {co2}")

            csv_writer.writerow([current_time, veh_id, co2])

        traci.simulationStep()

traci.close()

# Leer el archivo CSV
nombre_archivo_entrada = csv_file_path
datos = pd.read_csv(nombre_archivo_entrada)

# Calcular la CO2 promedio de cada vehículo
co2_promedio_por_vehiculo = datos.groupby('VehicleID')['CO2'].mean()

# Calcular la CO2 promedio general
co2_promedio_general = datos['CO2'].mean()

# Calcular el intervalo de confianza del 95% para el C02 promedio general
intervalo_confianza = stats.sem(datos['CO2']) * 1.96

# Crear la figura y los ejes
plt.figure(figsize=(12, 6))

# Gráfica 1: CO2 promedio de cada vehículo
plt.subplot(1, 2, 1)
sns.barplot(x=co2_promedio_por_vehiculo.index, y=co2_promedio_por_vehiculo.values)
plt.title('CO2 promedio por vehículo')
plt.xlabel('ID del vehículo')
plt.ylabel('CO2 (mg/s) promedio')

# Gráfica 2: CO2 promedio general con intervalo de confianza del 95%
plt.subplot(1, 2, 2)
plt.bar('CO2', co2_promedio_general, yerr=intervalo_confianza, color='skyblue', capsize=7)
plt.title('CO2 promedio general con IC 95%')
plt.ylabel('CO2 (mg/s) promedio')
plt.xticks([])

# Mostrar las gráficas
plt.tight_layout()
plt.show()
