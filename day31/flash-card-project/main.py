from tkinter import *
import pandas
from PIL import Image, ImageTk
import random

TIMER = 3000  # Default timer in milliseconds
BACKGROUND_COLOR = "#B1DDC6"
french_word_dict = {}  # list dictionary to store key:value as French:English word
new_dict = {}  # randomly picked key:value from french_word_dict

try:
    """ Load the contents in csv file to a dict using pandas, words_to_learn csv will contain only unknown words 
    when user clicks tick mark as considering it as known word and hence removing from the list """
    csv_data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    """ In case words_to_learn csv is not found then load the words having original words from french_words.csv """
    csv_data = pandas.read_csv("./data/french_words.csv")
    """ create the pair of the dict with key:value as French:English word in the form of list dictionary """
    french_word_dict = csv_data.to_dict(orient="records")
else:
    # french_word_dict = csv_data.to_dict()  # prints the complete set of data in the form of nested dict
    # print(french_word_dict)
    french_word_dict = csv_data.to_dict(orient="records")  # prints the data in the form dictionary inside list
    # print(french_word_dict)

""" picking a random French word from the list dictionary i.e. french_word_dict """


def card_picked():
    global new_dict, time_to_flip
    new_dict = random.choice(french_word_dict)
    """ User has an option to cancel the timer of 3s and wish to move onto next card """
    main_window.after_cancel(time_to_flip)
    # print(new_dict)
    """ using itemconfig method changing title to French and a word in french on every time we press the button """
    canvas.itemconfig(canv_title, text="French", fill="black")
    canvas.itemconfig(canv_word, text=new_dict["French"], fill="black")
    print(new_dict['French'])
    time_to_flip = main_window.after(TIMER, flip_card)


""" Flipping the card with a timer to see the English word """
def flip_card():
    # PhotoImage objects should not be created inside a function. Otherwise, it will not work.
    canvas.itemconfig(canv_title, text="English", fill="white")
    canvas.itemconfig(canv_word, text=new_dict["English"], fill="white")
    canvas.itemconfig(card_bg, image=card_back_img)
    print(new_dict['English'])


""" User knowing the french word """
def known_word():
    """  removes the randomly chosen French word and english word from the French word dictionary as
         user is aware of that word                                                                   """
    french_word_dict.remove(new_dict)
    print(len(french_word_dict))
    """ Creating a new csv file to update the known words into it """
    user_knows_word = pandas.DataFrame(french_word_dict)
    user_knows_word.to_csv("./data/words_to_learn.csv")

    """ Call the card_picked() to get the fresh word from the dictionary """
    card_picked()


""" Creating the main window for Flash Card """
main_window = Tk()
main_window.title("Flashy")
main_window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
""" a timer with 3s set where the card gets flipped to show the English word """
time_to_flip = main_window.after(TIMER, flip_card)

""" Creating Canvas for setting up the images """
canvas = Canvas(main_window, width=800, height=526)

# card_front_img = PhotoImage(file="./images/card_front.png")
card_front_img = ImageTk.PhotoImage(Image.open("./images/card_front.png"))
card_bg = canvas.create_image(400, 263, image=card_front_img)
canv_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
canv_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

# card_back_img = PhotoImage(file="./images/card_back.png")
card_back_img = ImageTk.PhotoImage(Image.open("./images/card_back.png"))
# card_back = canvas.create_image(400, 263, image=card_back_img) # not required as image can be switched to back image

canvas.grid(row=0, column=0, columnspan=2)

""" Creating buttons as image """
wrong_img = ImageTk.PhotoImage(Image.open("./images/wrong.png"))
wrong_button = Button(image=wrong_img, highlightthickness=0, command=card_picked)
wrong_button.grid(row=1, column=0)

right_img = ImageTk.PhotoImage(Image.open("./images/right.png"))
right_button = Button(image=right_img, highlightthickness=0, command=known_word)
right_button.grid(row=1, column=1)

""" Soon after the UI gets loaded on launch; display the card """
card_picked()

main_window.mainloop()
