from gpiozero import LightSensor
import matplotlib.pyplot as plt

ldr=LightSensor(4)

Iluminacion=['Lámpara apagada','Lámpara encendida','Luz celular']
Sensor=[]

print('Apague la luz')
input()
print(ldr.value)
x=ldr.value
print(x)
Sensor.append(x)
input()

print('Encienda la luz')
input()
x=ldr.value
print(x)
Sensor.append(x)
input()

print('Encienda la luz del celular')
input()
x=ldr.value
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