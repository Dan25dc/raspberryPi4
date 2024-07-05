import tkinter as tk

# Crear la ventana principal
gui_root = tk.Tk()
gui_root.iconbitmap("icono.ico")
gui_root.title("Interfaz de Control")
gui_root.geometry("500x200")
gui_root.configure(background="#24c5d4")
frame= tk.Frame(gui_root)
frame.pack(padx=5, pady=50)
# Crear los botones
boton_avanzar = tk.Button(frame, text="Avanzar" )
boton_retroceder = tk.Button(frame, text="Retroceder")
boton_parar = tk.Button(frame, text="Parar")
boton_detener = tk.Button(frame, text="Detener programa")

# Colocar los botones en la ventana
boton_avanzar.pack(side=tk.LEFT, padx=5, pady=5)
boton_retroceder.pack(side=tk.LEFT, padx=5, pady=5)
boton_parar.pack(side=tk.LEFT, padx=5, pady=5)
boton_detener.pack(side=tk.LEFT, padx=5, pady=5)
# Iniciar el bucle principal de la interfaz
gui_root.mainloop()