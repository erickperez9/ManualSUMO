# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from collections import defaultdict

def data_set(archivo_entrada): 
    # Nombre del archivo CSV de entrada y salida
    archivo_entrada = archivo_entrada
    archivo_salida = archivo_entrada
    
    # Cargar el archivo CSV en un DataFrame de pandas
    df = pd.read_csv(archivo_entrada)
    
    # Seleccionar solo las columnas 'vehicle_CO' y 'vehicle_type'
    columnas_a_mantener = ['tripinfo_id', 'emissions_fuel_abs', 'tripinfo_vType']
    df_filtrado = df[columnas_a_mantener]
    
    # Reemplazar los valores en la columna 'vType'
    mapeo = {'t_0': 1, 't_1': 2, 't_2': 3}
    df_filtrado['tripinfo_vType'] = df_filtrado['tripinfo_vType'].map(mapeo)
   
    # Eliminar las dos primeras filas
    df_filtrado = df_filtrado.iloc[2:]
    
    # Ordenar las filas según el valor de la tercera columna (vehicle_type)
    df_filtrado = df_filtrado.sort_values(by='tripinfo_vType', ascending=True)

    # Eliminar las filas que contienen 0 en la segunda columna
    # df_filtrado = df_filtrado[df_filtrado.iloc[:, 1] != 0]
    
    # Guardar el DataFrame filtrado en un nuevo archivo CSV
    #df_filtrado.to_csv(archivo_salida, index=False, header=False)
    
    # Convertir el DataFrame filtrado en un array de NumPy
    resultado_array = df_filtrado.to_numpy()
    
    # Creamos un diccionario para almacenar los valores de x basados en los valores de y
    X = resultado_array[:,[1]]
    print(X)
    y = np.asarray(resultado_array[:,2], dtype = 'int')
    valores_por_y = defaultdict(list)

    # Iteramos sobre x e y simultáneamente
    for valor_x, valor_y in zip(X, y):
        valores_por_y[valor_y].append(valor_x)

    # Calculamos la media para cada valor en y
    medias_por_y = {}
    for valor_y, valores_x in valores_por_y.items():
        medias_por_y[valor_y] = sum(valores_x) / len(valores_x)

    # Imprimimos los resultados       
    print("Se han eliminado las columnas excepto 'timestep_time' 'vehicle_CO' y 'vehicle_type'")
    print("Se han reemplazado los valores taxi, motorcycle, bus por 3,2,1.")
    for valor_y, media in medias_por_y.items():
        print(f"Media para y={valor_y}: {media}")
        
    return resultado_array
