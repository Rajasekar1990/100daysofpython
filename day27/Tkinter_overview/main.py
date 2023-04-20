import tkinter

# """ *args or multiple arguments in function example """
# def add(*args):
#     print(args)  # print all item in the args
#     print(args[0])  # prints the first arg in the args
#     print(type(args))  # prints the type of args i.e. a tuple in general
#     total1 = 0
#     """Looping through the numbers in args and adding all items"""
#     for num in args:
#         total1 += num
#     print(total1)
#
#     """Using list comprehension with sum() to calc the total"""
#     total = 0
#     total = [total + n for n in args]
#     return f"sum of all numbers is: {sum(total)}"
# print(add(2, 3, 6))
#
# """ **kwargs or keyword arguments example"""
# def calc(**kwargs):
#     print(kwargs)
#     result = {key: kwargs[key] for key in kwargs}
#     total = result["A"] + result["B"]
#     multiply = result["A"] * result["B"]
#     print(f"sum: {total}, product: {multiply}")
# calc(A=3, B=6)
#
# """ class creation with **(kwargs); same concept being used in Tkinter.label class taking unlimited kwargs"""
# class Myclass:
#     def __init__(self, **kw):
#         self.kwargs = kw
#         self.firstname = kw.get("fname")
#         self.lastname = kw.get("lname")
#
# myclass_obj = Myclass(fname="Rajasekar", lname="Sundararajan")
# print(myclass_obj.kwargs)
# print(myclass_obj.firstname + " " + myclass_obj.lastname)


""" Tk() class is used to inherit all the functionality of Tkinter """
my_GUI_window = tkinter.Tk()
""" give a title using title method """
my_GUI_window.title("Welcome to my GUI")
""" set the default size of window using minsize method """
my_GUI_window.minsize(width=400, height=400)
""" adding space on the border of screen to look you GUI legible"""
my_GUI_window.config(padx=20,pady=20)

""" Working with label """
my_label = tkinter.Label(text="This is a Label", highlightbackground="white", font=("Courier", 24))
"""to change/update/replace the values for kwargs in the label then use any of the below methods"""
my_label["text"] = "*** New Text ***"
my_label.config(text="This ia a Label")
""" pack method is used to keep a single component in the desired place of your screen window"""
# my_label.pack(side="left")
""" place method is used keep the component in the precise location using x and y coord on your screen window"""
# my_label.place(x=0,y=0)
""" Grid method imagines the entire UI in the form of grid with col and row representation """
my_label.grid(column=0, row=0)

""" Working with Button """
my_button = tkinter.Button(text="OK")
# my_button.pack(side="left")
# my_button.place(x=25,y=25)
my_button.grid(column=1, row=1)

""" adding a new button to place in column 2 of grid """
my_button1 = tkinter.Button(text="Cancel")
my_button1.grid(column=2, row=0)

""" Working with Entry class, used for creating textbox for receiving input """
user_input = tkinter.Entry(width=10)
# user_input.pack(side="left")
# user_input.place(x=50, y=50)
user_input.grid(column=3, row=2)

# Add some text to begin with
# user_input.insert(END, string="Some text to begin with.")

def click():
    input_val = user_input.get()
    my_label.config(text=f"{input_val}")

""" On clicking the OK button should update the label with user input given """
my_button.config(text="OK", command=click)

# """ Text Box example """
# text = tkinter.Text(height=5, width=30)
# # Puts cursor in textbox.
# text.focus()
# # Adds some text to begin with.
# text.insert(END, "Example of multi-line text entry.")
# # Get's current value in textbox at line 1, character 0
# print(text.get("1.0", END))
# text.pack()
#
# """ Spinbox"""
# def spinbox_used():
#     # gets the current value in spinbox.
#     print(spinbox.get())
# spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()
#
# """ Scale bar with current value displayed """
# #Called with current scale value.
# def scale_used(value):
#     print(value)
# scale = tkinter.Scale(from_=0, to=100, command=scale_used)
# scale.pack()
#
# """ Checkbutton """
# def checkbutton_used():
#     # Prints 1 if On button checked, otherwise 0.
#     print(checked_state.get())
# # variable to hold on to checked state, 0 is off, 1 is on.
# checked_state = IntVar()
# checkbutton = tkinter.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()
#
#
# """ Radiobutton """
# def radio_used():
#     print(radio_state.get())
# radio_state = IntVar()
# radiobutton1 = tkinter.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = tkinter.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()
#
# """ Listbox """
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))
#
# listbox = tkinter.Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()

""" main loop method is to hold the screen without exiting """
my_GUI_window.mainloop()
