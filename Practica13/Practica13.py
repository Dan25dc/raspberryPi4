from tkinter import *
from gpiozero import DistanceSensor

ultrasonic = DistanceSensor(echo=24, trigger=23)

def funDistancia():
    d = round (ultrasonic.distance * 100, 2)
    v.set ("La distancia es {}cm ".format(d))
    labelDistancia.after(500, funDistancia)

#crear la ventana
root = Tk()
root.title('Sensor Ultrasonico')
root.geometry('300x50+60+60')

frame = Frame(root)
frame.grid(row = 0, column = 0, sticky = W+N, padx = 10, pady = 10)

v = StringVar()
v.set('Espere, porfavor!')
labelDistancia = Label(frame, textvariable = v)
labelDistancia.grid(row=0, column=0, sticky=W)

labelDistancia.after(500, funDistancia)
root.mainloop()
