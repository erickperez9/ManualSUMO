# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 16:03:37 2024

@author: PCX
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

# Cargar el archivo CSV
df = pd.read_csv('tripinfo-emissions.csv')

# Eliminar filas con valores faltantes en las columnas relevantes
df.dropna(subset=['emissions_CO2_abs', 'tripinfo_vType'], inplace=True)

# Seleccionar características (emisiones CO2 absolutas) y etiquetas (tipo de vehículo)
X = df[['emissions_CO2_abs']]
y = df['tripinfo_vType']

# Codificar las etiquetas de texto a números
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Definir diccionario para mapear los números de clase a tipos de vehículos
clase_vehiculo = {0: 'bus', 1: 'taxi', 2: 'motorcycle'}

# Inicializar y entrenar el modelo RandomForestClassifier
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Inicializar y entrenar el modelo LogisticRegression
lr_model = LogisticRegression(max_iter=1000, random_state=42)
lr_model.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred_rf = rf_model.predict(X_test)
y_pred_lr = lr_model.predict(X_test)

# Evaluar el rendimiento de Random Forest
print("Random Forest Classifier:")
print("Accuracy Score:", accuracy_score(y_test, y_pred_rf))
print("\nClassification Report:\n", classification_report(y_test, y_pred_rf))

# Evaluar el rendimiento de Logistic Regression
print("\nLogistic Regression:")
print("Accuracy Score:", accuracy_score(y_test, y_pred_lr))
print("\nClassification Report:\n", classification_report(y_test, y_pred_lr))

# Graficar las predicciones
plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='black', label='Verdadero')  # Datos verdaderos
plt.scatter(X_test, y_pred_rf, color='red', label='RF Predicho')  # Predicciones RF
plt.scatter(X_test, y_pred_lr, color='blue', label='LR Predicho')  # Predicciones LR
plt.title('Comparación de Emisiones de CO2 Verdaderas vs Predichas')
plt.xlabel('Emisiones de CO2')
plt.ylabel('Tipo de Vehículo Predicho')

# Modificar las etiquetas del eje Y para indicar el tipo de vehículo
plt.yticks([0, 1, 2], [clase_vehiculo[i] for i in [0, 1, 2]])

# Mostrar la gráfica
plt.legend()
plt.show()
