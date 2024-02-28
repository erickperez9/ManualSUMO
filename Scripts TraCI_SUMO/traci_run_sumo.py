import traci

traci.start(["sumo", "-c", "/home/sumo/sumo/tools/2024-02-05-16-21-35/osm.sumocfg"])

while traci.simulation.getMinExpectedNumber() > 0:
    traci.simulationStep()
    
traci.close()
