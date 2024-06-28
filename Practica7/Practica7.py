# Temperatura, Hora
from gpiozero import CPUTemperature
from time import sleep, strftime, time
cpu= CPUTemperature()
cpu.temperature()
strftime("%H:%M:%S")
type (strftime("%H:%M:%S"))
a= strftime("%H:%M:%S")
a
n= int (input("Ingrese la cantidad de alumnos \n"))
print(n)

Nombre= []
Hora= []

for x in range(n):
    nom = input("Nombre del alumno: ")
    Nombre.append(nom)
    h= strftime("%H:%M:%S")
    print(h)
    Hora.append(h)

print(Nombre)
