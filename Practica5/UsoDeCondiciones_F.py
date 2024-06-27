from gpiozero import LED, Button

led= LED(17)
button = Button(2)

while True:

    if button.is_pressed:
        led.on()
        print("Se presionó el botón y encendió el led")
    else:
        led.off()
        print("No se ha presionado el botón, ni encendido el led")
        