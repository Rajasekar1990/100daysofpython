import math
from tkinter import *
from PIL import ImageTk, Image

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
MY_TIMER = None
REPS = 0

# ---------------------------- TIMER RESET ------------------------------- #
"""Creating a function for user to perform reset of timer on clicking reset button"""
def reset_timer():
    main_window.after_cancel(MY_TIMER) # after_cancel method helps to stop the pause given in main_window.after method
    """Set the label back to TIMER """
    timer_label.config(text="TIMER", fg=GREEN)

    """ Set the timer to 00:00 """
    canvas.itemconfig(timer_text_var, text="00:00")

    """ Remove all the tick marks"""
    tick_label.config(text="", padx=10, pady=10, fg=GREEN, bg=YELLOW)

    """ Reset the REPS value to 0"""
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
""" Creating a timer function to manage the timer """
def countdown_timer(timer_val):
    """ to represent the time in mm:ss below actions will to be performed """
    mm = math.floor(timer_val / 60)  # floor method will round down the val to the nearest whole number
    # if mm / 60 < 10: # using dynamic mapping change the format from 0:0 to 00:00
    #     mm = f"0{mm}"
    ss = timer_val % 60  # takes the reminder which is the remaining seconds
    """using dynamic mapping change the format from 0:0 to 00:00"""
    if ss < 10: # datatype is int
        ss = f"0{ss}" # datatype becomes str
    """itemconfig method helps to update the canvas text with timer value in dynamic fashion"""
    canvas.itemconfig(timer_text_var, text=f"{mm}:{ss}")
    if timer_val > 0:
        # after method helps to perform any activity with a pause given in milliseconds
        global MY_TIMER
        MY_TIMER = main_window.after(1000, countdown_timer, timer_val - 1)
    else: # calling start_timer() to follow the pomodoro reps
        start_timer()
        # creating a new var called No_of_ticks to count num of times work timer is complete
        No_of_ticks = ""
        # 2 times WORK timer completion is equal to 1 iteration of pomodoro is completed hence REPS/2
        WORK_REPS = math.floor(REPS / 2)
        for ticks in range(WORK_REPS):
            No_of_ticks += "✓"
        # on every 2 WORK timer run, 1 tick mark will be added to the screen
        tick_label.config(text=No_of_ticks, padx=10, pady=10, fg=GREEN, bg=YELLOW)

"""Creating a function for user to perform start timer action on clicking start button"""
def start_timer():
    global REPS
    REPS += 1
    # if REPS is one of 1, 3, 5, 7 .... then WORK_MIN timer should run
    if REPS % 2 != 0:
        countdown_timer(WORK_MIN * 60)
        timer_label.config(text="WORK", fg=GREEN)
    # if REPS is one of 2, 4, 6, 10 .... then SHORT_BREAK_MIN timer should run
    elif ((REPS % 2 == 0) and (REPS % 8 != 0)):
        countdown_timer(SHORT_BREAK_MIN * 60)
        timer_label.config(text="BREAK", fg=PINK)
    # if REPS is one of 8, 16, 24 ..... then LONG_BREAK_MIN timer should run
    else:
        countdown_timer(LONG_BREAK_MIN)
        timer_label.config(text="BREAK", fg=RED)

# ---------------------------- UI SETUP ------------------------------- #
""" Tk class """
main_window = Tk()
main_window.title("Pomodoro")
""" apply yellow background using bg arg"""
main_window.config(padx=100, pady=50, bg=YELLOW)

"""
**** Canvas Class ****
Set the screen size using canvas class for keeping tomato img as a background
Apply yellow background using bg arg also, highlight thickness arg helps to get rid of border thickness """
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
"""read an image file and store them into a var using PhotoImage Class"""
# tomato_img = PhotoImage(file="tomato.png")
# canvas.create_image(103, 224, image=tomato_img)
tomato_img = ImageTk.PhotoImage(Image.open("tomato.png"))  # PIL solution
canvas.create_image(100, 112, image=tomato_img) # x=100 and y=112 half of canvas width and height respectively

"""Creating the text 00:00 with tomato image as background"""
timer_text_var = canvas.create_text(100, 112, text="00:00", fill="red", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

"""Creating a label for TIMER """
timer_label = Label(text="Timer", padx=10, pady=10, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0)

"""Creating a button for START and RESET"""
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

"""Creating a label for Tick mark"""
tick_label = Label(padx=10, pady=10, fg=GREEN, bg=YELLOW)
tick_label.grid(column=1, row=3),

main_window.mainloop()
