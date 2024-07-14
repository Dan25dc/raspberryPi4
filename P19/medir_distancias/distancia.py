# Importa las bibliotecas necesarias
from datetime import datetime
import pandas as pd
import sys
from gpiozero import DistanceSensor
import mysql.connector

# Parámetro de distancia (simulado para propósitos de prueba)
ultrasonic = DistanceSensor(echo=17, trigger=4)
distance = int(round(ultrasonic.distance * 100))

# Obtiene la fecha y hora actuales
fecha = datetime.now().strftime('%Y/%m/%d')
hora = datetime.now().strftime('%H:%M:%S')

# Crea un DataFrame con los datos actuales
data = {"CM": [distance], "FECHA": [fecha], "HORA": [hora]}
df_actual = pd.DataFrame(data)

# Intenta cargar el archivo CSV existente si ya existe
try:
    df_previo = pd.read_csv("distancias.csv")
    df_nuevo = pd.concat([df_previo, df_actual], ignore_index=True)
except FileNotFoundError:
    # Si el archivo no existe aún, crea uno nuevo con los datos actuales
    df_nuevo = df_actual

# Guarda el DataFrame actualizado en el archivo CSV
df_nuevo.to_csv("distancias.csv", index=False)

# Imprime el resultado para que pueda ser capturado por PHP (opcional)
print(f'<h1 style="color: blue; text-align: center;">La distancia medida es: {distance} cm</h1>')
print(f'<h2 style="color: blue; text-align: center;">Fecha: {fecha}, Hora: {hora} </h2>')


# Intentar establecer la conexión a la base de datos
try:
    bd = mysql.connector.connect(
        host="localhost",
        user="sensor",
        password='1234',
        database="SENSORES"
    )
except mysql.connector.Error as err:
    sys.exit(1)  # Salir del programa si hay un error de conexión

cursor = bd.cursor()

# Si se pudo obtener la distancia, proceder con el registro en la base de datos
if distance is not None:
    sql = "INSERT INTO DISTANCIA (CM, FECHA, HORA) VALUES(\""+str(distance)+"\",\""+str(datetime.now().strftime('%Y-%m-%d'))+"\",\""+str(datetime.now().strftime('%H:%M:%S'))+"\");"

    try:
        # Ejecutar el comando SQL
        cursor.execute(sql)
        # Hacer efectivos los cambios en la base de datos
        bd.commit()
        print(f'<h2 style="color: brown; text-align: center;">Los datos se guardaron en archivo csv y base de datos.</h2>')
    except mysql.connector.Error as err:
        print(f'<h2 style="color: brown; text-align: center;">Error al guardar en la base de datos: {err} </h2>')
        bd.rollback()  # Deshacer la operación si hay un error en la inserción
else:
    print ('Falló obtener la lectura')
