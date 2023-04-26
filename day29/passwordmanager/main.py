from tkinter import *  # Astrix imports only all classes and constants
from tkinter import messagebox  # importing messagebox module
from PIL import Image, ImageTk
import random
import pyperclip
default_Username = "rajasekar.s1@idfcbank.com"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_gen():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
               'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
               'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    special_char = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+"]

    """ Conventional list creation using simple for loop """
    # for character in range(0, random.randint(8, 32)):
    #     final_password.append(random.choice(letters))

    """ for loop using list comprehension """
    # final_password = [random.choice(letters) for _ in range(0, random.randint(8, 32))]
    pwd_letter = [random.choice(letters) for _ in range(0, random.randint(8, 10))]
    pwd_num = [random.choice(numbers) for _ in range(0, 2)]
    pwd_special_char = [random.choice(special_char) for _ in range(0, 2)]

    """ Concatenating all the lists and shuffling them to create the final pwd """
    final_password = pwd_letter + pwd_num + pwd_special_char
    random.shuffle(final_password)

    password_entry.insert(0, f"{''.join(final_password)}")
    # print(f"{''.join(final_password)}")

    """ holding the final pwd generated in the clipboard """
    pyperclip.copy(f"{''.join(final_password)}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pwd():
    """ Get the current text from entry boxes """
    website_text = website_entry.get()
    username_text = username_entry.get()
    password_text = password_entry.get()

    """ Check if there are any empty fields Website or password entry boxes """
    if website_text == "" or password_text == "":
        messagebox.showinfo(title="Oops!", message="Please fill all the entries")
    else:
        """ Creating a pop up for user to confirm their details before adding them to data.txt"""
        save = messagebox.askokcancel(title=website_text,
                                      message=f"These are the details entered\n"
                                              f"email: {username_text}\n"
                                              f"password: {password_text}\nDo you want to save?")

        if save:
            """ Writing website | username | password information to data.txt file """
            with open(file="data.txt", mode="a") as pwd_file_handler:
                pwd_file_handler.write(f"{website_text} || {username_text} || {password_text}\n")

            """Deleting all entries post updating the details in data.txt file"""
            website_entry.delete(0, END)
            username_entry.delete(0, END)
            password_entry.delete(0, END)
            username_entry.insert(END, default_Username)


# ---------------------------- UI SETUP ------------------------------- #
""" Creating main window """
main_window = Tk()
main_window.config(padx=50, pady=50)
# main_window.geometry('1000x1000')
# main_window.minsize(width=500, height=500)
main_window.title("Password Manager")

""" Creating canvas widget for placing the logo """
canv = Canvas(main_window, width=200, height=200)
""" Loading the image """
logo = ImageTk.PhotoImage(Image.open("logo.png"))
""" Adding image to the Canvas Items """
canv.create_image(100, 100, anchor=CENTER, image=logo)
canv.grid(column=1, row=0)

""" Creating label - WEBSITE """
website_label = Label(text="Website:", anchor="center", pady=5, highlightthickness=0, font=("Arial", 12))
website_label.grid(column=0, row=1)

""" Creating label - Email/Username """
username_label = Label(text="Email/Username:", anchor="center", pady=5, highlightthickness=0, font=("Arial", 12))
username_label.grid(column=0, row=2)

""" Creating label - Password """
password_label = Label(text="Password:", anchor="center", pady=5, highlightthickness=0, font=("Arial", 12))
password_label.grid(column=0, row=3)

""" Creating textbox for WEBSITE entry """
website_entry = Entry(main_window, width=41, highlightthickness=0)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()  # placing the cursor in the website entry box during the start

""" Creating textbox for Email/Username entry """
username_entry = Entry(main_window, width=41, highlightthickness=0)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(END, default_Username)  # insert method can help in setting a default value

""" Creating textbox for Password entry """
password_entry = Entry(main_window, width=25, highlightthickness=0)
password_entry.grid(column=1, row=3)

""" Creating a button - Generate Password """
gen_pwd_button = Button(text="Generate Password", width=14, highlightthickness=0,
                        font=("Arial", 12), command=password_gen)
gen_pwd_button.grid(column=2, row=3)

""" Creating a button - Add """
add_button = Button(text="Add", width=44, highlightthickness=0, font=("Arial", 12), command=save_pwd)
add_button.grid(column=1, row=4, columnspan=2)

main_window.mainloop()
