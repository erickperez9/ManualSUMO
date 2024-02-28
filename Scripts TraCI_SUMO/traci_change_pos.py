import traci
import csv
import time


#traci.close()

# Iniciar la conexión
traci.start(["sumo", "-c", "/home/sumo/sumo/tools/2024-02-05-16-21-35/osm.sumocfg"])

csv_file_path = 'datos_change_pos.csv'

with open(csv_file_path, 'w', newline='') as csvfile:
    
    csv_writer = csv.writer(csvfile)

    # Cabecera del CSV
    csv_writer.writerow(['Time', 'VehicleID', 'Speed', 'EdgeNow'])

    # Ejecutar la simulación 
    while traci.simulation.getMinExpectedNumber() > 0:
        current_time = traci.simulation.getCurrentTime() / 1000  # Convertir a segundos

        for veh_id in traci.vehicle.getIDList():
            speed = traci.vehicle.getSpeed(veh_id)  
            edgeNow = traci.vehicle.getRoadID(veh_id)
            
            if veh_id == "veh424" and speed > 10:
            	traci.vehicle.changeTarget(veh_id,"234463928#1")
            	print(f"**** SE HA CAMBIADO LA RUTA DEL VEHICULO {veh_id} HACIA 234463928#1")
                     
            print(f"Tiempo: {current_time}, ID del Vehículo: {veh_id}, Velocidad: {speed}, EdgeNow: {edgeNow}")
        
            csv_writer.writerow([current_time, veh_id, speed,edgeNow])

        traci.simulationStep()

traci.close()


