import tkinter as tk
from PIL import ImageTk, Image

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

MotorEncendido="lightblue"
MotorApagado="lightblue"

Vacio="lightblue"
Lleno="lightblue"

pathImagen="img/Inicial.jpg"

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

gui_root.mainloop()
