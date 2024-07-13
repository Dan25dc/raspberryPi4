from gpiozero import DistanceSensor
import RPi.GPIO as GPIO
import tkinter as tk
from PIL import ImageTk, Image
from time import sleep

# Configura sensor ultrasónico
ultrasonic = DistanceSensor(echo=17, trigger=4)

# Configuración de pines GPIO
GPIO.setmode(GPIO.BOARD)
Motor1A = 16
Motor1B = 18
Motor1E = 22
GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
GPIO.setup(Motor1E, GPIO.OUT)

GPIO.output(Motor1E,GPIO.LOW)

def avanzar():
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.HIGH)

def parar():
    GPIO.output(Motor1E,GPIO.LOW)

def PedirDistancia():
    # Realiza la medición de distancia
    cm =int(round(ultrasonic.distance*100))
    if (cm > 5.0):
        avanzar()
        print(f'{cm}, Llenando ...')
    elif (cm < 5.0):
        parar()
        print(f'{cm}, Apagando...')
    
    indicatorL_label.config(text="Nivel: "+str(cm))
    return cm

# Variables globales iniciales
Vacio = "lightblue"
Lleno = "lightblue"
MotorEncendido = "lightblue"
MotorApagado = "lightblue"
pathImagen = "img/Inicial.jpg"

def ActualizaImagen():
    # Actualizar la imagen
    try:
        img = ImageTk.PhotoImage(Image.open(pathImagen))
        img_label.config(image=img)
        img_label.image = img  # mantener referencia para evitar garbage collection
    except Exception as e:
        # Manejar el caso donde no se encuentra la imagen
        error_label.config(text="Imagen no encontrada")

def ActualizaEtiquetas():
    # Actualizar los indicadores
    indicator1_label.config(bg=Vacio)
    indicator2_label.config(bg=Lleno)
    indicator3_label.config(bg=MotorEncendido)
    indicator4_label.config(bg=MotorApagado)

def actualizar_indicadores():
    global Dist, Vacio, Lleno, MotorEncendido, MotorApagado, pathImagen
    # Lógica para actualizar los valores de Vacio, Lleno, MotorEncendido, MotorApagado y pathImagen
    Contador=PedirDistancia()
    print(Contador)

    if (Contador > 5):
        Vacio = "#48EC2B"
        Lleno = "lightblue"
        MotorApagado = "lightblue"
        MotorEncendido = "#48EC2B"
        ActualizaEtiquetas()
        pathImagen = "img/1.jpg"
        ActualizaImagen()
        gui_root.after(1000, ActualizaImagen)
        pathImagen = "img/2.jpg"
        ActualizaImagen()
        gui_root.after(2000, ActualizaImagen)
        pathImagen = "img/3.jpg"
        gui_root.after(3000, ActualizaImagen)
        
    elif (Contador < 5):
        Vacio = "lightblue"
        Lleno = "#48EC2B"
        MotorApagado = "#48EC2B"
        MotorEncendido = "lightblue"
        ActualizaEtiquetas()
        pathImagen = "img/4.jpg"
        ActualizaImagen()

    else:
        MotorApagado = "lightblue"
        MotorEncendido= "lightblue"
        Vacio = "lightblue"
        Lleno = "lightblue"
        pathImagen = "img/Inicial.jpg"

    # Llamar a la función nuevamente después de 2000 ms (2 segundos)
    gui_root.after(2000, actualizar_indicadores)

def iniciar_sistema():
    # Iniciar la función para actualizar indicadores
    actualizar_indicadores()

# Crear la ventana principal
gui_root = tk.Tk()
gui_root.title("Control de llenado")
gui_root.configure(background="white")

# Establecer el tamaño de la ventana
window_width = 1024
window_height = 640
gui_root.geometry(f"{window_width}x{window_height}")

# Obtener el tamaño de la pantalla
screen_width = gui_root.winfo_screenwidth()
screen_height = gui_root.winfo_screenheight()

# Calcular la posición de la ventana para centrarla
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Establecer la geometría de la ventana con la posición calculada
gui_root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Añadir un título
title_label = tk.Label(gui_root, text="Sistema para el control de llenado de tanque", font=("Arial", 24), bg="white", fg="blue")
title_label.pack(pady=20)

# Crear un marco para dividir la pantalla en dos
left_frame = tk.Frame(gui_root, bg="white")
right_frame = tk.Frame(gui_root, bg="white")

left_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)
right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

# Añadir la imagen en el left_frame (izquierda)
try:
    img = ImageTk.PhotoImage(Image.open(pathImagen))
    img_label = tk.Label(left_frame, image=img, bg="white")
    img_label.pack(expand=True)
except Exception as e:
    error_label = tk.Label(left_frame, text="Imagen no encontrada", font=("Arial", 16), bg="white", fg="red")
    error_label.pack(expand=True)

# Crear indicadores en el right_frame (derecha)
indicatores1 = tk.Label(right_frame, text="Indicador de nivel", font=("Arial", 20), bg="white", fg="purple")
indicatores1.pack(pady=5)

# Crear marco para el primer indicador
indicator1_frame = tk.Frame(right_frame, bg="lightblue", pady=10, padx=10)
indicator1_frame.pack(pady=20, fill="x")

indicator1_label = tk.Label(indicator1_frame, text="Tanque vacío", font=("Arial", 18), bg=Vacio, fg="black")
indicator1_label.pack()

indicator2_label = tk.Label(indicator1_frame, text="Tanque lleno", font=("Arial", 18), bg=Lleno, fg="black")
indicator2_label.pack()

indicatorL_label = tk.Label(indicator1_frame, text="Nivel", font=("Arial", 18), bg="lightblue", fg="black")
indicatorL_label.pack()

# Crear indicadores en el right_frame (derecha)
indicatores2 = tk.Label(right_frame, text="Indicador de motor", font=("Arial", 20), bg="white", fg="purple")
indicatores2.pack(pady=5)

# Crear marco para el segundo indicador
indicator2_frame = tk.Frame(right_frame, bg="lightblue", pady=10, padx=10)
indicator2_frame.pack(pady=20, fill="x")

indicator3_label = tk.Label(indicator2_frame, text="Motor encendido", font=("Arial", 18), bg=MotorEncendido, fg="black")
indicator3_label.pack()

indicator4_label = tk.Label(indicator2_frame, text="Motor apagado", font=("Arial", 18), bg=MotorApagado, fg="black")
indicator4_label.pack()

# Añadir el botón de iniciar en el right_frame (derecha)
start_button = tk.Button(right_frame, text="Iniciar", font=("Arial", 20), bg="green", fg="white", command=iniciar_sistema)
start_button.pack(pady=20)

# Ejecutar la ventana principal
gui_root.mainloop()
