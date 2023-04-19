from turtle import Turtle, Screen
import pandas

t_obj = Turtle()
t_obj.shape("square")

s_obj = Screen()

# adding a title to your screen
s_obj.title("U.S. States Game")

# adding a gif file image using add shape method
img_file_path = "blank_states_img.gif"
s_obj.addshape(img_file_path)
t_obj.shape(img_file_path)

# # get the x,y coordinates of mouse click on the image
# def mouse_click(x, y):
#     print(x, y)
#
#
# # onscreenclick method helps to keep the screen as is without exiting
# s_obj.onscreenclick(mouse_click)
# turtle.mainloop()

score = 0

# count the number of answered states by the user
guessed_state = []

# read the csv using pandas and store the csv data in data var
data = pandas.read_csv("50_states.csv")

# getting the list of states and converting them to a list
data_list = data["state"].to_list()

# asking user to guess the state name
while len(guessed_state) < 50:
    answer = s_obj.textinput(title=f"{len(guessed_state)}/50 States Correct", prompt="Enter the State Name").title()
    print(answer.lower())

    if answer in data_list:
        t = Turtle()
        t.hideturtle()
        t.penup()
        row_data = data[data["state"] == answer]
        t.goto(x=int(row_data["x"]), y=int(row_data["y"]))
        t.write(answer, move=True, align="center", font=('courier', 8, 'normal'))
        guessed_state.append(answer)

    # Method 1:
    if answer == "Exit":
        # Method 1 using normal list with for loop to go through list items:
        missed_state = []
        for state in data_list:
            if state not in guessed_state:
                missed_state.append(state)

        # Method 2 using list comprehension:
        missed_state = [state for state in data_list if state not in guessed_state]

        list_data = pandas.DataFrame(missed_state)
        list_data.to_csv("missed_states.csv")
        break
