import matplotlib.pyplot as plt
datos = [(1, 1), (2, 2), (3, 3),(4, 4),(5, 5),(6, 6),(7, 7),(8, 8),(9, 9),(10, 10)]

x=[]
y=[]

for elem in datos:
    x.append(elem[0])
    y.append(elem[1])

print(x)
print(y)

plt.plot(x,y, marker='o')
plt.xlabel('Valor1')
plt.ylabel('Valor2')
plt.title('Gráfica')
plt.show()