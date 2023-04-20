from tkinter import *

"""Creating Main Window which is of 500*300 px"""
main_window = Tk()
main_window.minsize(width=500, height=300)
main_window.config(padx=15, pady=15)
main_window.title("Miles to Km Convertor")

"""Creating entry1 for entering the user input in Miles"""
entry1 = Entry(width=10)
entry1.grid(column=1, row=0)

"""Creating Label1=is equal to"""
label1 = Label()
label1.config(text="is equal to", padx=10, pady=10, font=("Arial", 15))
label1.grid(column=0, row=1)

"""Creating Label2=Miles"""
label2 = Label()
label2.config(text="Miles", padx=10, pady=10, font=("Arial", 15))
label2.grid(column=2, row=0)

"""Creating Label3=Km"""
label3 = Label()
label3.config(text="Km", padx=10, pady=10, font=("Arial", 15))
label3.grid(column=2, row=1)


def click_calculate():
    val = float(entry1.get())
    if val == 1.0:
        label2.config(text="Mile")
    kms = round(val * 1.609, 1)
    # print(kms)
    label3.config(text=f"{kms}")


"""Creating label3 for updating output in Kms"""
label3 = Label(text="0", padx=10, pady=10, font=("Arial", 15))
label3.grid(column=1, row=1)

"""Creating Button=Calculate"""
button = Button(text="Calculate", width=10, padx=10, pady=10, font=("Arial", 15, "bold"))
button.config(text="Calculate", command=click_calculate)
button.grid(column=1, row=2)


main_window.mainloop()
