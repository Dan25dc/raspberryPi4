import RPi.GPIO as GPIO
import tkinter as tk
import time
import pandas as pd
from datetime import datetime

# Configuración de pines GPIO
GPIO.setmode(GPIO.BOARD)
Motor1A = 16
Motor1B = 18
Motor1E = 22
GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
GPIO.setup(Motor1E, GPIO.OUT)

# Inicialización de variables
data = []
Start_Time = None
Last_Button = None

def calcular_tiempo():
    global Start_Time
    End_Time = time.monotonic()
    Transcurrido = int(round(End_Time - Start_Time))
    return Transcurrido

def actualizar_tiempo(boton_actual):
    global Start_Time, Last_Button
    if Start_Time is not None and Last_Button is not None:
        Transcurrido = calcular_tiempo()
        print(f"Tiempo transcurrido en {Last_Button}: {Transcurrido} segundos")
        data.append({"Sentido":Last_Button, "Duracion": Transcurrido, "Hora": time.strftime("%H:%M:%S")})

        print(f'Sentido de giro: {Last_Button}, Duracion: {Transcurrido}, Hora: {time.strftime("%H:%M:%S")}')
    Start_Time = time.monotonic()
    Last_Button = boton_actual

def avanzar():
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.HIGH)
    print("Estás en avanzar")
    actualizar_tiempo("Avanzar")

def retroceder():
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
    GPIO.output(Motor1E,GPIO.HIGH)
    print("Estás en retroceder")
    actualizar_tiempo("Retroceder")

def parar():
    GPIO.output(Motor1E,GPIO.LOW)
    print("Estás en parar")
    actualizar_tiempo("Detenido")

def detener():
    global Start_Time, Last_Button
    GPIO.output(Motor1E,GPIO.LOW)

    print("Has detenido el programa")
    if Start_Time is not None and Last_Button is not None:
        Transcurrido = calcular_tiempo()
        print(f"Tiempo transcurrido en {Last_Button}: {Transcurrido} segundos")
        
        data.append({"Sentido":Last_Button, "Duracion": Transcurrido, "Hora": time.strftime("%H:%M:%S")})
        print(f'Sentido de giro: {Last_Button}, Duracion: {Transcurrido}, Hora: {time.strftime("%H:%M:%S")}')
        Start_Time = None
        Last_Button = None

        GPIO.cleanup()

        # Obtener la fecha y hora actual
        fecha_actual = datetime.now().strftime('%Y-%m-%d')
        hora_actual = datetime.now().strftime('%H-%M-%S')

        # Nombre del archivo CSV con fecha y hora
        nombre_archivo = f'datosMotor_{fecha_actual}_{hora_actual}.csv'

        # Crear un DataFrame a partir de la lista de datos
        df = pd.DataFrame(data)
    
        # Guardar el DataFrame en un archivo CSV
        df.to_csv(nombre_archivo, index=False)
        print(f"Datos guardados en '{nombre_archivo}'.")

    else:
        print("Cronómetro ya estaba detenido")


# Crear la ventana principal
root = tk.Tk()
root.title("Controlador")

# Crear los botones
boton_avanzar = tk.Button(root, text="Avanzar", command=avanzar)
boton_retroceder = tk.Button(root, text="Retroceder", command=retroceder)
boton_parar = tk.Button(root, text="Parar", command=parar)
boton_detener = tk.Button(root, text="Detener", command=detener)

# Colocar los botones en la ventana
boton_avanzar.pack(side=tk.LEFT, padx=5, pady=5)
boton_retroceder.pack(side=tk.LEFT, padx=5, pady=5)
boton_parar.pack(side=tk.LEFT, padx=5, pady=5)
boton_detener.pack(side=tk.LEFT, padx=5, pady=5)
# Iniciar el bucle principal de la interfaz
root.mainloop()