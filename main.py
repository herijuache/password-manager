import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    # List comprehensions
    letter_list = [choice(letters) for _ in range(nr_letters)]
    symbol_list = [choice(symbols) for _ in range(nr_symbols)]
    number_list = [choice(numbers) for _ in range(nr_numbers)]

    password_list = letter_list + symbol_list + number_list
    shuffle(password_list)

    password = "".join(password_list)

    entry_password.delete(0, END)
    entry_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = entry_website.get().title()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Missing File", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showerror(title="No Match", message=f"No details for {website} exists.")


# ---------------------------- SHOW ALL ------------------------------- #
def get_all():
    # Prompt user to create txt file containing all passwords
    create_file = messagebox.askyesno(title="Create New File", message="Create text file with all inputted passwords?")
    if create_file:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            messagebox.showerror(title="Error", message="No data file found")
        else:
            with open("all_passwords.txt", "w") as file:
                for website in data:
                    email = data[website]["email"]
                    password = data[website]["password"]
                    file.write(f"{website}\n"
                               f"--------------------------\n"
                               f"Email: {email}\n"
                               f"Password: {password}\n"
                               f"--------------------------\n")
            messagebox.showinfo(title="Success!", message="Text file created:)")


# ---------------------------- SAVE PASSWORD ------------------------------- #
# Create a function that'll take in:
# name of website, email/username, password
def add_info():
    website = entry_website.get().title()
    userinfo = entry_userinfo.get()
    password = entry_password.get()
    new_data = {
        website: {
            "email": userinfo,
            "password": password
        }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as file:
                # Write
                # json.dump(new_data, file, indent=4)
                # Read
                data = json.load(file)
                # print(data)
                # Update
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        finally:
            entry_website.delete(0, END)
            entry_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

# Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)  # (xpos, ypos, image)
canvas.grid(row=0, column=1)

# Labels
lbl_website = Label(text="Website:")
lbl_website.grid(row=1, column=0)
lbl_userinfo = Label(text="Email/Username:")
lbl_userinfo.grid(row=2, column=0)
lbl_password = Label(text="Password:")
lbl_password.grid(row=3, column=0)

# Entries
entry_website = Entry(width=30)
entry_website.focus()
entry_website.grid(row=1, column=1)
entry_userinfo = Entry(width=48)
entry_userinfo.grid(row=2, column=1, columnspan=2)
entry_userinfo.insert(0, "testemail@gmail.com")  # placeholder email
entry_password = Entry(width=30)
entry_password.grid(row=3, column=1)

# Buttons
btn_search = Button(text="Search", width=14, command=find_password)
btn_search.grid(row=1, column=2, pady=5)
btn_password = Button(text="Generate Password", command=generate_password)
btn_password.grid(row=3, column=2, pady=5)
btn_add = Button(text="Add", width=41, command=add_info)
btn_add.grid(row=4, column=1, columnspan=2)
btn_show_all = Button(text="Get All Passwords", width=41, command=get_all)
btn_show_all.grid(row=5, column=1, columnspan=2)

window.mainloop()
