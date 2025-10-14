import turtle
from tkinter import Button

# Funktion für den OK-Button
def on_ok():
    print("OK-Button wurde gedrückt!")
    turtle.clear()
    turtle.hideturtle()
    turtle.write("OK gedrückt!", font=("Arial", 16, "normal"))

# Funktion für den Cancel-Button
def on_cancel():
    print("Cancel-Button wurde gedrückt!")
    turtle.clear()
    turtle.hideturtle()
    turtle.write("Cancel gedrückt!", font=("Arial", 16, "normal"))

# Turtle Screen erstellen
screen = turtle.Screen()
screen.title("Turtle mit Buttons")

# Zugriff auf das zugrunde liegende Tkinter-Fenster
canvas = screen.getcanvas()
tk = canvas.winfo_toplevel()

# OK-Button hinzufügen
ok_button = Button(tk, text="OK", command=on_ok)
ok_button.pack(side="right", padx=10, pady=10)

# Cancel-Button hinzufügen
cancel_button = Button(tk, text="Cancel", command=on_cancel)
cancel_button.pack(side="bottom", padx=10, pady=10)

# Turtle-Loop starten
turtle.mainloop()