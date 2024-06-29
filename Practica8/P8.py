from gpiozero import DistanceSensor
import pandas as pd
from datetime import datetime
import time
import numpy as np
import matplotlib.pyplot as plt

ultrasonic=DistanceSensor(echo=17, trigger=4)

datos = {'item': [], 'distancia': [], 'fecha': [], 'hora': []}
columnas = ['item', 'distancia', 'fecha', 'hora']
distancias=[]

df = pd.DataFrame(columns=columnas)  # Crear un DataFrame vacío

contador = 0

def CrearGraficos():
    # Cantidad de datos
    cantidad_datos = np.arange(1, len(distancias) + 1)

    # Crear una figura con dos subplots en una fila
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))

    # Gráfico de dispersión
    axs[0].scatter(cantidad_datos, distancias)
    axs[0].plot(cantidad_datos, distancias, linestyle="solid", color="red")
    axs[0].set_xlabel("No. de lecturas")
    axs[0].set_ylabel("Distancia")
    axs[0].set_title("Gráfico de dispersión de los datos")

    # Crear una Serie con las frecuencias
    frecuencias = pd.Series(distancias).value_counts()

    # Filtrar solo las frecuencias de 90, 75, 60, 45, 30, 15
    #frecuencias_filtradas = frecuencias.loc[[90, 75, 60, 45, 30, 15]]

    # Gráfico de barras
    axs[1].bar(frecuencias.index, frecuencias.values, align='center', width=0.5, color='skyblue', edgecolor='red')
    axs[1].set_xlabel("Distancia")
    axs[1].set_ylabel("Frecuencia")
    axs[1].set_title("Tabla de Frecuencia de Distancias")
    axs[1].grid(axis='y')

    # Ajustar el espacio entre subplots
    plt.tight_layout()

    # Mostrar la figura con ambos subplots
    plt.show()

try:
    while contador != 60:
        # Leer la distancia del sensor
        distancia = int(round(ultrasonic.distance))
        distancias.append(distancia)

        # Obtener la fecha y hora actual
        fecha = datetime.now().strftime('%Y-%m-%d')
        hora = datetime.now().strftime('%H:%M:%S')

        contador += 1

        # Agregar los datos al DataFrame
        lectura = {'item': contador, 'distancia': distancia, 'fecha': fecha, 'hora': hora}
        df = pd.concat([df, pd.DataFrame([lectura])], ignore_index=True)

        # Imprimir los valores leídos en la consola
        print(f'item: {contador}, distancia: {distancia}, Fecha: {fecha}, Hora: {hora}')

        # Esperar un segundo antes de la siguiente lectura
        time.sleep(1)

except Exception as e:
    print(f"Ocurrió un error: {e}")
finally:
    # Obtener la fecha y hora actual
    fecha_actual = datetime.now().strftime('%Y-%m-%d')
    hora_actual = datetime.now().strftime('%H-%M-%S')

    # Nombre del archivo CSV con fecha y hora
    nombre_archivo = f'datos_{fecha_actual}_{hora_actual}.csv'

    # Guardar el DataFrame en un archivo CSV
    df.to_csv(nombre_archivo, index=False)
    print(f"Datos guardados en '{nombre_archivo}'.")

    try:
        CrearGraficos()
    except Exception as e:
        print(f"No se pueden crear los gráficos, erorr de lectura: ",e)