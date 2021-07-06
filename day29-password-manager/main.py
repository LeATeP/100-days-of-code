from tkinter import *
from tkinter import messagebox as ms
import random
import json
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def rand_password():
    letters_rand = [random.choice(letters) for _ in range(random.randint(8, 10))]
    numbers_rand = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    symbols_rand = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_list = letters_rand + numbers_rand + symbols_rand
    random.shuffle(password_list)
    rand_pass = ''.join(password_list)

    pyperclip.copy(rand_pass)
    entry_pass.delete(0, END)
    return entry_pass.insert(0, rand_pass)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def file_operation(new_data):
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
            data.update(new_data)

    except FileNotFoundError:
        with open("data.json", mode="w") as data_file:
            json.dump(new_data, data_file, indent=4)

    else:
        with open("data.json", mode="w") as data_file:
            json.dump(data, data_file, indent=4)

    finally:
        entry_website.delete(0, END)
        entry_pass.delete(0, END)


def save():
    web_text = entry_website.get()
    user_name = entry_user.get()
    pass_gen = entry_pass.get()
    new_data = {web_text: {
        "user_name": user_name,
        "pass_gen": pass_gen,
    }}

    if web_text != "" and pass_gen != "" and user_name != "":
        confirmation = ms.askquestion(title="Confirmation", message="Save it?")

        if confirmation == "yes":
            file_operation(new_data)
    else:
        ms.showwarning("error", "Website or Pass is Empty")

    return


def search():
    web_text = entry_website.get()
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        ms.showinfo(title="Error", message="No data was found")

        if web_text in data:
            print("good")
            ms.showinfo(title="info", message=f"Your Email: {data[web_text]['user_name']}\n"
                                              f"Your Pass: {data[web_text]['pass_gen']}\n"
                                              f"\nYour pass has been saved in Tray")
            pyperclip.copy(data[web_text]['pass_gen'])
        else:
            ms.showwarning(title="Error", message="nothing has been found")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)
# ----------------------

label_website = Label(text="Website")
label_website.grid(column=0, row=1)

label_user = Label(text="Email/Username")
label_user.grid(column=0, row=2)

label_pass = Label(text="Password")
label_pass.grid(column=0, row=3)
# ----------------------

button_gen = Button(text="Generate Password", command=rand_password)
button_gen.grid(column=2, row=3)

button_add = Button(text="Add", command=save)
button_add.grid(column=1, row=4, columnspan=2)
button_add.config(width=35)

button_search = Button(text="Search", command=search)
button_search.grid(column=2, row=1, columnspan=2)
button_search.config(width=14)
# ----------------------

entry_website = Entry()
entry_website.grid(column=1, row=1)
entry_website.config(width=21)

entry_user = Entry()
entry_user.grid(column=1, row=2, columnspan=2)
entry_user.config(width=35)
entry_user.insert(0, "leateps@gmail.com")

entry_pass = Entry()
entry_pass.grid(column=1, row=3)
entry_pass.config(width=21)

window.mainloop()
