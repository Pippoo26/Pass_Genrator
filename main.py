from tkinter import *
from tkinter import messagebox
import json
from random import randint, choice, shuffle


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_gen():
    pass_ent.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_sysmbol = [choice(symbols) for _ in range(randint(2, 4))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_sysmbol + password_number
    shuffle(password_list)

    password = "".join(password_list)

    pass_ent.insert(0, password)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_pass():
    website = web_ent.get()

    try:
        with open("passwords.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="file not found")
    else:
        if website in data:
            email = data[website]["username"]
            password = data[website]["password"]
            messagebox.showinfo(title="INFO", message=f"ID = {email} \n pass= {password}")
        else:
            messagebox.showinfo(title="error", message="recheck your website name, and try again")


# ---------------------------- SAVE PASSWORD ------------------------------- #
is_it_ok = True
filled = True


def save():
    global is_it_ok
    global filled
    website = web_ent.get()
    email = id_ent.get()
    password = pass_ent.get()
    new_data = {website:
        {
            "username": email,
            "password": password,
        }
    }
    try:
        with open("passwords.json", "r") as data_f:
            data = json.load(data_f)

    except FileNotFoundError:
        with open("passwords.json", "w") as data_f:
            json.dump(new_data, data_f, indent=4)
    else:
        if email == "" or password == "":
            messagebox.showinfo(title="Error", message="You just leave something empty, plz fill it to save")
            filled = False

        if filled:
            if website in data:
                is_it_ok = messagebox.askokcancel(message="data is alredy present in file, U want to override it???")

        if is_it_ok:
            is_oki = messagebox.askokcancel(title=f"{website}", message=f"This are the details u just entered: \n"
                                                                        f"Id: {email} \n"
                                                                        f"password: {password} \n"
                                                                        f"is it all okay to save???")
            if is_oki:
                data.update(new_data)
                with open("passwords.json", "w") as data_f:
                    json.dump(data, data_f, indent=4)

    finally:
        is_it_ok = True
        web_ent.delete(0, END)
        pass_ent.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=20, pady=20)
window.title("Password Manager")

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

web_lab = Label(text="Website: ")
id_lab = Label(text="Email/Username:")
pass_lab = Label(text="Password:")

web_lab.grid(column=0, row=1)
id_lab.grid(column=0, row=2)
pass_lab.grid(column=0, row=3)

web_ent = Entry(width=28, )
web_ent.focus()
id_ent = Entry(width=46)
pass_ent = Entry(width=27)

web_ent.place(x=97, y=206)
id_ent.place(x=97, y=228)
pass_ent.place(x=97, y=250)

pass_gen_btn = Button(text="Generate Password", command=pass_gen)
pass_gen_btn.place(x=267, y=247, )
add_btn = Button(text="Add", width=39, command=save)
add_btn.grid(column=1, row=5, columnspan=2, )

search_btn = Button(text="Search", width=14, command=find_pass)
search_btn.place(x=270, y=201)

window.mainloop()

