from tkinter import *
import random

window = Tk()
window.title("Mile to Km converter")
window.minsize(250, 200)
window.config(padx=20, pady=20)

#############################
# Label
button_miles = Label(text="Mile", font=("Arial", 10))
button_miles.place(x=150, y=5)
# my_label["text"] = "New label"
# or 
# my_label.config(text="My new label")

#############################
# Button


def convert():
    user_input = entry.get()
    covert = float(user_input) * 1.6
    button_result["text"] = covert


button = Button(text="Calculate", command=convert)
button.place(x=80, y=70)

# Entry
entry = Entry()
entry.place(x=80, y=10)
entry.config(width=10)
#############################

button_equal = Label(text="is equal to", font=("Arial", 10))
button_equal.place(x=10, y=40)
button_result = Label(text="0", font=("Arial", 10))
button_result.place(x=100, y=40)
button_km = Label(text="Km", font=("Arial", 10))
button_km.place(x=150, y=40)





window.mainloop()
