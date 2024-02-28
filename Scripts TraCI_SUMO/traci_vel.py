import traci
import csv
import time
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


#traci.close()

# Iniciar la conexión
traci.start(["sumo", "-c", "/home/sumo/sumo/tools/2024-02-05-16-21-35/osm.sumocfg"])

csv_file_path = 'datos_simulacion_vel.csv'
with open(csv_file_path, 'w', newline='') as csvfile:
    
    csv_writer = csv.writer(csvfile)

    # Cabecera del CSV
    csv_writer.writerow(['Time', 'VehicleID', 'Speed'])

    # Ejecutar la simulación 
    while traci.simulation.getMinExpectedNumber() > 0:
        current_time = traci.simulation.getCurrentTime() / 1000  # Convertir a segundos

        for veh_id in traci.vehicle.getIDList():
            speed = traci.vehicle.getSpeed(veh_id)            
            print(f"Tiempo: {current_time}, ID del Vehículo: {veh_id}, Velocidad: {speed}")
        
            csv_writer.writerow([current_time, veh_id, speed])

        traci.simulationStep()

traci.close()

# Leer el archivo CSV
nombre_archivo_entrada = csv_file_path
datos = pd.read_csv(nombre_archivo_entrada)

# Calcular la velocidad promedio de cada vehículo
velocidad_promedio_por_vehiculo = datos.groupby('VehicleID')['Speed'].mean()

# Calcular la velocidad promedio general
velocidad_promedio_general = datos['Speed'].mean()

# Calcular el intervalo de confianza del 95% para la velocidad promedio general
intervalo_confianza = stats.sem(datos['Speed']) * 1.96

# Crear la figura y los ejes
plt.figure(figsize=(12, 6))

# Gráfica 1: Velocidad promedio de cada vehículo
plt.subplot(1, 2, 1)
sns.barplot(x=velocidad_promedio_por_vehiculo.index, y=velocidad_promedio_por_vehiculo.values)
plt.title('Velocidad promedio por vehículo')
plt.xlabel('ID del vehículo')
plt.ylabel('Velocidad (m/s) promedio')

# Gráfica 2: Velocidad promedio general con intervalo de confianza del 95%
plt.subplot(1, 2, 2)
plt.bar('Velocidad promedio', velocidad_promedio_general, yerr=intervalo_confianza, color='skyblue', capsize=7)
plt.title('Velocidad promedio general con IC 95%')
plt.ylabel('Velocidad (m/s) promedio')
plt.xticks([])

# Mostrar las gráficas
plt.tight_layout()
plt.show()
