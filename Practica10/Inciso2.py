import tkinter as tk
from tkinter import ttk, messagebox

def do_booking():
    messagebox.showinfo("Booking", "Thank you for booking")
    print(film_choice.get())
    print(vip_seat_var.get())
    print(row_choice_var.get())

app = tk.Tk()
app.title("My second GUI app")
app.geometry("300x200")

# Film Choice
film_description = tk.Label(app, text="Which film?")
film_description.grid(row=0, column=0, sticky="w")
film_choice = ttk.Combobox(app, values=["Star Wars", "Frozen", "Lion King"])
film_choice.grid(row=0, column=1, sticky="w")

# VIP Seat
vip_description = tk.Label(app, text="Seat type")
vip_description.grid(row=1, column=0, sticky="w")
vip_seat_var = tk.IntVar()
vip_seat = tk.Checkbutton(app, text="VIP seat?", variable=vip_seat_var)
vip_seat.grid(row=1, column=1, sticky="w")

# Row Choice
set_description = tk.Label(app, text="Seat location")
set_description.grid(row=2, column=0, sticky="w")
row_choice_var = tk.StringVar(value="M")
row_choice_frame = tk.Frame(app)
row_choice_frame.grid(row=2, column=1, sticky="w")
front_radio = tk.Radiobutton(row_choice_frame, text="Front", variable=row_choice_var, value="F")
front_radio.pack(side="left")
middle_radio = tk.Radiobutton(row_choice_frame, text="Middle", variable=row_choice_var, value="M")
middle_radio.pack(side="left")
back_radio = tk.Radiobutton(row_choice_frame, text="Back", variable=row_choice_var, value="B")
back_radio.pack(side="left")

# Book Seats Button
book_seats = tk.Button(app, text="Book seat", command=do_booking)
book_seats.grid(row=3, column=1, sticky="w")

app.mainloop()
