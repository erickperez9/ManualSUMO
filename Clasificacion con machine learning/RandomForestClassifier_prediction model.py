import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
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

# Inicializar y entrenar el modelo RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = model.predict(X_test)

# Evaluar el rendimiento del modelo
print("Accuracy Score:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Graficar las predicciones
# Definir diccionario para mapear los números de clase a tipos de vehículos
clase_vehiculo = {0: 'bus', 1: 'taxi', 2: 'motorcycle'}

# Convertir las clases predichas de números a tipos de vehículos
y_pred_labels = [clase_vehiculo[i] for i in y_pred]

# Graficar las predicciones
plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='black', label='Verdadero')  # Datos verdaderos
plt.scatter(X_test, y_pred, color='red', label='Predicho')  # Predicciones
plt.title('Comparación de Emisiones de CO2 Verdaderas vs Predichas')
plt.xlabel('Emisiones de CO2')
plt.ylabel('Tipo de Vehículo Predicho')

# Modificar las etiquetas del eje Y para indicar el tipo de vehículo
plt.yticks([0, 1, 2], [clase_vehiculo[i] for i in [0, 1, 2]])

# Mostrar la gráfica
plt.legend()
plt.show()
