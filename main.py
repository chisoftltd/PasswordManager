from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=YELLOW)

key_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=250, bg=YELLOW)
canvas.create_image(100, 112, image=key_image)
canvas.create_text(100, 12, text="Password Manager", fill="red", font=(FONT_NAME, 15, "bold"))
canvas.grid(column=1, row=0)

site_label = Label(text="WebSite:", font=(FONT_NAME, 10, "bold"))
site_label.grid(row=2, column=0)

site_entry = Entry(width=52)
site_entry.grid(row=2, column=1, columnspan=2)

email_label = Label(text="Email/Username: ", font=(FONT_NAME, 10, "bold"))
email_label.grid(row=3, column=0)

email_entry = Entry(width=52)
email_entry.grid(row=3, column=1, columnspan=2)

pwd_label = Label(text="Password", font=(FONT_NAME, 10, "bold"))
pwd_label.grid(row=4, column=0)

pwd_entry = Entry(width=33)
pwd_entry.grid(row=4, column=1)

pwd_button = Button(text="Generate Password")
pwd_button.grid(row=4, column=2)

add_button = Button(text="Add", width=44)
add_button.grid(row=5, column=1, columnspan=2)

window.mainloop()
