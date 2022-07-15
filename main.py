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
    letter_list = [choice(letters) for char in range(nr_letters)]
    symbol_list = [choice(symbols) for char in range(nr_symbols)]
    number_list = [choice(numbers) for char in range(nr_numbers)]

    password_list = letter_list + symbol_list + number_list
    shuffle(password_list)

    password = "".join(password_list)

    entry_password.delete(0, END)
    entry_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
# Create a function that'll take in:
# name of website, email/username, password
def add_info():
    website = entry_website.get()
    userinfo = entry_userinfo.get()
    password = entry_password.get()

    # Show error box
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        # Check if user is happy with info
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n{userinfo}"
                                                              f"\nPassword: {password} \nIs it ok to save?")

        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {userinfo} | {password}\n")
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
entry_website = Entry(width=45)
entry_website.focus()
entry_website.grid(row=1, column=1, columnspan=2)
entry_userinfo = Entry(width=45)
entry_userinfo.grid(row=2, column=1, columnspan=2)
entry_userinfo.insert(0, "testemail@gmail.com")  # placeholder email
entry_password = Entry(width=27)
entry_password.grid(row=3, column=1)

# Buttons
btn_password = Button(text="Generate Password", command=generate_password)
btn_password.grid(row=3, column=2)
btn_add = Button(text="Add", width=39, command=add_info)
btn_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
