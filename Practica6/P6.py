import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

# Define el pin al que esta conectado el circuito
pin_to_circuit = 4

Iluminacion=['Lámpara apagada','Lámpara encendida','Luz celular']
Sensor=[]

def rc_time (pin_to_circuit):
    count = 0
  
    # Salida para el pin
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    # Se cambia el pin de nuevo a entrada 
    GPIO.setup(pin_to_circuit, GPIO.IN)
  
    # Contar hasta que el pin se ponga en alto
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1

    return count

print('Apague la luz')
input()
x=rc_time(pin_to_circuit)
print(x)
Sensor.append(x)
input()

print('Encienda la luz')
input()
x=rc_time(pin_to_circuit)
print(x)
Sensor.append(x)
input()

print('Encienda la luz del celular')
input()
x=rc_time(pin_to_circuit)
print(x)
Sensor.append(x)
input()

print(Iluminacion)
print(Sensor)

fig=plt.figure()
ax=fig.add_subplot(111)
xx=range(1,len(Sensor)+1)

ax.bar(xx,Sensor,width=0.5,color=(0,0,1),align='center')
ax.set_xticks(xx)
ax.set_xticklabels(Iluminacion)
ax.set_ylabel('Sensor')

plt.show()

GPIO.cleanup()