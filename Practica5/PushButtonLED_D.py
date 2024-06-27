from gpiozero import LED,Button
from time import sleep

led=LED(17)
button=Button(2)

while True:

    print()
    print()
    print('No se ha presionado el botón')
    print()
    print()

    a=button.wait_for_press()

    print(a,', se ha presionado el botón')
    print()

    b=led.on()

    print(b,', se ha encendido el led 5 seg.')
    print()

    sleep(5)
    print('hola, después de 5 seg.')
    led.off()

    button.wait_for_release()
    print()
    print('se ha soltado el botón y apagado el led')