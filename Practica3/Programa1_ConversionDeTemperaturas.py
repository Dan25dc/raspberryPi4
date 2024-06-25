
def inicio():
    n = int( input("\n Seleccione \n 1.Celsius a Farenheit \n 2.Farenheit a Celsius \n"))
    print()

    if (n==1):
        c = float ( input("Ingrese la temperatura en grados Celsius \n"))
        f = c * (9/5) + 32
        print ( str(c) + "°C equivalen a " + str(f) + "°F")
        print()

    if (n==2):
        f = float ( input("Ingrese la temperatura en grados Farenheit \n"))
        c = (f-32) * (5/9)
        print ( str(f) + "°F equivalen a " + str(c) + "°C")
        print()

    return repetir()

def repetir():

    while True:
        again = input ("Continuar (y/n) ?: ")
        if again not in {"y","n"}:
            print ("ingrese (y/n): ")
        elif again == "y":
            return inicio()
        elif again == "n":
            return "adios"
inicio()
        