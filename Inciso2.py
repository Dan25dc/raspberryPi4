import tkinter as tk
from tkinter import ttk, messagebox

def do_booking():
    messagebox.showinfo("Reservando", "Gracias por reservar")
    print(film_choice.get())
    print(vip_seat_var.get())
    print(row_choice_var.get())

app = tk.Tk()
app.title("Mi segunda aplicación GUI")
app.geometry("300x200")

# Film Choice
film_description = tk.Label(app, text="¿Cuál película?")
film_description.grid(row=0, column=0, sticky="w")
film_choice = ttk.Combobox(app, values=["Star Wars", "Frozen", "El Rey León"])
film_choice.grid(row=0, column=1, sticky="w")

# VIP Seat
vip_description = tk.Label(app, text="Tipo de asiento")
vip_description.grid(row=1, column=0, sticky="w")
vip_seat_var = tk.IntVar()
vip_seat = tk.Checkbutton(app, text="¿Asiento VIP?", variable=vip_seat_var)
vip_seat.grid(row=1, column=1, sticky="w")

# Row Choice
set_description = tk.Label(app, text="Ubicación del asiento")
set_description.grid(row=2, column=0, sticky="w")
row_choice_var = tk.StringVar(value="M")
row_choice_frame = tk.Frame(app)
row_choice_frame.grid(row=2, column=1, sticky="w")
front_radio = tk.Radiobutton(row_choice_frame, text="Hasta frente", variable=row_choice_var, value="AD")
front_radio.pack(side="left")
middle_radio = tk.Radiobutton(row_choice_frame, text="En medio", variable=row_choice_var, value="ME")
middle_radio.pack(side="left")
back_radio = tk.Radiobutton(row_choice_frame, text="Hasta atrás", variable=row_choice_var, value="AT")
back_radio.pack(side="left")

# Book Seats Button
book_seats = tk.Button(app, text="Reservar asiento", command=do_booking)
book_seats.grid(row=3, column=1, sticky="w")

app.mainloop()
