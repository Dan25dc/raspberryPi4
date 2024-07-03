import tkinter as tk

def say_my_name():
    welcome_message.config(text=my_name.get())

def change_text_size(slider_value):
    welcome_message.config(font=("Times New Roman", slider_value))

app = tk.Tk()
app.title("Tamaño de una etiqueta")

welcome_message = tk.Label(app, text="Bienvenido a mi app, escribe tu nombre", font=("Times New Roman", 15), fg="#80d2d2")
my_name = tk.Entry(app, width=10)
update_text = tk.Button(app, command=say_my_name, text="Muestra mi nombre")
text_size = tk.Scale(app, from_=10, to=80, command=change_text_size)
my_cat = tk.PhotoImage(file="Raspberry.png")

# Create a label widget to display the image (you can use a Canvas widget for more flexibility)
my_cat_label = tk.Label(app, image=my_cat)
my_cat_label.photo = my_cat  # Keep a reference to prevent garbage collection

# Pack widgets
welcome_message.pack()
my_name.pack()
update_text.pack()
text_size.pack()
my_cat_label.pack()

app.mainloop()

