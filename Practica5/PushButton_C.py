from gpiozero import Button

button=Button(2)

while True:
    print()
    print()
    print()
    print('No se ha presionado el botón')

    a=button.wait_for_press()

    print()
    print(a,' se ha presionado el botón')
    print()

    button.wait_for_release()
    print('Se ha soltado el botón')