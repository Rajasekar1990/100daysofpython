from tkinter import *  # Astrix imports only all classes and constants
from tkinter import messagebox  # importing messagebox module
from PIL import Image, ImageTk
import random
import pyperclip
import json

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
    website_text = website_entry.get().lower()
    username_text = username_entry.get()
    password_text = password_entry.get()

    """ create a dictionary for storing details to use in json module"""
    json_dict = {
        website_text: {
            "email": username_text,
            "password": password_text,
        }
    }

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
            try:
                """ Writing website | username | password information to data.txt file """
                with open(file="data.json", mode="r") as data_read:
                    """ if the file exists then continue with reading the content """
                    json_content = json.load(fp=data_read)
                    # print(json_content)
                    # print(type(json_content))

            except FileNotFoundError:
                """ Creates a new file when data.json is not found """
                with open(file="data.json", mode="w") as data_write:
                    """ write the new data using dump method """
                    json.dump(obj=json_dict, fp=data_write, indent=4)

            else:
                """ this block gets executed when file exists by saving the udpated data to existing data.json """
                # update the json content with new data and save it to json file using json.dump
                json_content.update(json_dict)
                with open(file="data.json", mode="w") as data_update:
                    json.dump(obj=json_content, fp=data_update, indent=4)

            finally:
                """Deleting all entries post updating the details in data.txt file"""
                website_entry.delete(0, END)
                username_entry.delete(0, END)
                password_entry.delete(0, END)
                username_entry.insert(END, default_Username)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    search_text = website_entry.get().lower()
    try:  # try opening the data.json file instead of executing them for sure all the time
        with open(file="data.json", mode="r") as data_read:
            password_data = json.load(data_read)
        # print(password_data)
    except FileNotFoundError:  # handling if the data.json itself is not found
        messagebox.showinfo(title="Info!", message="No data file found")
    else:
        if search_text in password_data:  # check for website entered is present in data.json
            email_found = password_data[search_text]["email"]  # nested dictionary hence 2 keys req to get email
            password_found = password_data[search_text]["password"]
            # message pops up with the email and password for the entered website name
            messagebox.showinfo(title=search_text, message=f"email: {email_found}\n password: {password_found}")
        else:
            # throwing a message popup in case of no entries found
            messagebox.showinfo(title="Error!", message=f"0 entries found for {search_text}")
    finally:
        # Deleting the entry in website text box
        website_entry.delete(0, END)


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
website_entry = Entry(main_window, width=25, highlightthickness=0)
website_entry.grid(column=1, row=1)
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

""" Creating a button - Search """
search_button = Button(text="Search", width=14, highlightthickness=0,
                       font=("Arial", 12), command=find_password)
search_button.grid(column=2, row=1)

main_window.mainloop()
