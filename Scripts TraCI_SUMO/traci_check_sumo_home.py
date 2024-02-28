import traci
import sys
import os

def verificar_variable_entorno(variable):
    valor = os.getenv(variable)
    if valor is not None:
        print(f'La variable de entorno {variable} está definida.')
        print(f'Su valor es: {valor}\n')
    else:
        print(f'La variable de entorno {variable} no está definida.\n')

if __name__ == "__main__":
    variable_entorno = "SUMO_HOME"
    verificar_variable_entorno(variable_entorno)
    
    print("LOADPATH:", '\n'.join(sys.path))
    print("TRACIPATH:", traci.__file__)
    sys.exit()





