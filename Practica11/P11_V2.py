import RPi.GPIO as GPIO
import time 
import pandas as pd
from datetime import datetime

GPIO.setmode(GPIO.BOARD)

Motor1A = 16
Motor1B = 18
Motor1E = 22

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)


print("Avanzar")
GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor1B,GPIO.LOW)
GPIO.output(Motor1E,GPIO.HIGH)
time.sleep(3)
horaAvance=time.strftime("%H:%M:%S")

print("Retroceder")
GPIO.output(Motor1A,GPIO.LOW)
GPIO.output(Motor1B,GPIO.HIGH)
GPIO.output(Motor1E,GPIO.HIGH)
time.sleep(3)
horaRetoceso=time.strftime("%H:%M:%S")


print("Detener motor")
GPIO.output(Motor1E,GPIO.LOW)

GPIO.cleanup()

# Crear una lista para almacenar los datos
data = []

# Agregar datos para el sentido de giro, la duración y la hora
data.append({"Sentido de giro": "Avanzar", "Duracion": 3, "Hora": horaAvance})
data.append({"Sentido de giro": "Retroceder", "Duracion": 3, "Hora": horaRetoceso})

# Crear un DataFrame a partir de la lista de datos
df = pd.DataFrame(data)

# Obtener la fecha y hora actual
fecha_actual = datetime.now().strftime('%Y-%m-%d')
hora_actual = datetime.now().strftime('%H-%M-%S')

# Nombre del archivo CSV con fecha y hora
nombre_archivo = f'datosMotor_{fecha_actual}_{hora_actual}.csv'

# Guardar el DataFrame en un archivo CSV
df.to_csv(nombre_archivo, index=False)
print(f"Datos guardados en '{nombre_archivo}'.")
