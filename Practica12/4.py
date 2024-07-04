import matplotlib.pyplot as plt
n = int (input("Ingrese la cantidad de alumnos \n"))
print(n)

Nombres= []
Calificacion= []

for x in range(n):
    nom = input("Nombre del alumno: ")
    Nombres.append(nom)
    cal = int(input("Calificacion: "))
    Calificacion.append(cal)

print(Nombres)
print (Calificacion)

fig= plt.figure()
ax= fig.add_subplot(111)

datos= [2,4,6,8,10]
xx= range (1,len(Calificacion)+1)

ax.bar(xx,Calificacion, width=0.5, color=(0,0,1), align= 'center')
ax.set_xticks(xx)
ax.set_xticklabels(Nombres)
ax.set_ylabel('Calificaciones')

plt.show()
