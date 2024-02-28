import traci
import csv
import time
import re


# Iniciar la conexión
traci.start(["sumo", "-c", "/home/sumo/sumo/tools/2024-02-05-16-21-35/osm.sumocfg"])

# Lista de identificadores de vehículos
lista_veh = []

# Ejecutar la simulación 
while traci.simulation.getMinExpectedNumber() > 0:
	for veh_id in traci.vehicle.getIDList():
	    #print(f"ID del Vehículo: {veh_id}")
	    lista_veh.append(veh_id)


	traci.simulationStep()

traci.close()

# Expresión regular para encontrar los números en los identificadores de vehículos
patron = re.compile(r'veh(\d+)')

# Inicializamos el máximo como cero
maximo = 0

# Iteramos sobre la lista de vehículos
for vehiculo in lista_veh:
    # Buscamos los números en los identificadores de vehículos usando expresiones regulares
    match = patron.match(vehiculo)
    if match:
        numero = int(match.group(1))  # Convertimos el número a entero
        maximo = max(maximo, numero)  # Actualizamos el máximo

print(f"\n En el mapa han circulado un total de {maximo} vehículos")

