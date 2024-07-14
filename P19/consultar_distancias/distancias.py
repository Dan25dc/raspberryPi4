import mysql.connector
from mysql.connector import Error
import sys
import json

# Función para conectar a la base de datos
def conectar_bd():
    try:
        bd = mysql.connector.connect(
            host="localhost",
            user="sensor",
            password="1234",
            database="SENSORES"
        )
        return bd
    except Error as e:
        print("Error de conexión:", e)
        sys.exit(1)

# Función para realizar la búsqueda según el tipo especificado
def buscar_datos(busqueda, tipo_busqueda):
    try:
        conexion = conectar_bd()
        cursor = conexion.cursor(dictionary=True)

        if tipo_busqueda == "todos":
            consulta = "SELECT * FROM DISTANCIA"
            cursor.execute(consulta)
        elif tipo_busqueda == "distancia":
            consulta = "SELECT * FROM DISTANCIA WHERE CM = %s"
            cursor.execute(consulta, (busqueda,))
        elif tipo_busqueda == "fecha":
            consulta = "SELECT * FROM DISTANCIA WHERE FECHA = %s"
            cursor.execute(consulta, (busqueda,))
        elif tipo_busqueda == "hora":
            consulta = "SELECT * FROM DISTANCIA WHERE HORA = %s"
            cursor.execute(consulta, (busqueda,))
        elif tipo_busqueda == "count":
            consulta = "SELECT COUNT(*) AS total FROM DISTANCIA"
            cursor.execute(consulta)
            resultado = cursor.fetchone()
            total=str(resultado['total'])  # Devolver el resultado como texto
            return '<h3 style="color: green">Total de datos = '+total+'</h3>'  # Devolver el resultado como texto
        elif tipo_busqueda == "max":
            consulta = "SELECT MAX(CM) AS maximo FROM DISTANCIA"
            cursor.execute(consulta)
            resultado = cursor.fetchone()
            max= str(resultado['maximo'])  # Devolver el resultado como texto
            return '<h3 style="color: green">La distancia máxima es = '+max+'</h3>'  # Devolver el resultado como texto
        elif tipo_busqueda == "min":
            consulta = "SELECT MIN(CM) AS minimo FROM DISTANCIA"
            cursor.execute(consulta)
            resultado = cursor.fetchone()
            min=str(resultado['minimo'])
            return '<h3 style="color: green">La distancia mínima es = '+min+'</h3>'  # Devolver el resultado como texto
        elif tipo_busqueda == "avg":
            consulta = "SELECT AVG(CM) AS promedio FROM DISTANCIA"
            cursor.execute(consulta)
            resultado = cursor.fetchone()
            prom= str(resultado['promedio'])
            return '<h3 style="color: green">El promedio de distancias es = '+prom+'</h3>'  # Devolver el resultado como texto
        else:
            print("Tipo de búsqueda no válido")
            sys.exit(1)

        registros = cursor.fetchall()
        conexion.close()

        # Convertir los registros a formato JSON y devolver como texto
        return json.dumps(registros)

    except Error as e:
        print("Error en la consulta:", e)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: distancias.py <busqueda> <tipo_busqueda>")
        sys.exit(1)

    busqueda = sys.argv[1]
    tipo_busqueda = sys.argv[2]

    datos = buscar_datos(busqueda, tipo_busqueda)
    print(datos)  # Imprimir el resultado
