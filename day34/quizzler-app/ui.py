from tkinter import *
from quiz_brain import QuizBrain
from PIL import Image, ImageTk
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain): # text: datatype
        self.quiz = quiz_brain
        self.main_window = Tk()
        self.main_window.title("Quiz Game")
        # self.main_window.minsize(width=500, height=500)
        self.main_window.config(padx=20, pady=20, bg=THEME_COLOR)

        """ Creating Label for Score card on right top corner """
        self.scorecard = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.scorecard.grid(column=1, row=0)

        """ Creating a Canvas object for Quiz question display """
        self.canvas = Canvas(self.main_window, width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="Sample Text",
                                                     fill=THEME_COLOR,
                                                     width= 280, # set a width to display with wrap text in canvas box
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50) # set padding above and below the canvas grid

        """ Creating a tick button with True image for choosing True/False """
        true_button_img = ImageTk.PhotoImage(Image.open("./images/true.png"))
        self.true_button = Button(image=true_button_img, highlightthickness=0, command=self.true_button_click)
        self.true_button.grid(column=0, row=2)

        """ Creating a cross button with False image for choosing True/False """
        false_button_img = ImageTk.PhotoImage(Image.open("./images/false.png"))
        self.false_button = Button(image=false_button_img, highlightthickness=0, command=self.false_button_click)
        self.false_button.grid(column=1, row=2)

        """ Calling next_question_method for questions from question bank """
        self.next_question_method()

        self.main_window.mainloop()

    """ Creating next question method """
    def next_question_method(self):
        """ setting the bg back to white after canvas turns to green/red based on user's answer """
        self.canvas.config(bg="white")
        """ Checking the length of question from question_list """
        if self.quiz.still_has_questions():
            """ resetting the scorecard based on user answer """
            self.scorecard = Label(text=f"Score: {self.quiz.score}")
            """ Calling next_question fn which is inside quiz_brain """
            q_text = self.quiz.next_question() # store the output in q_text
            """ call canvas object to config the q.no and question text """
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of quiz")
            """ disable the buttons after the quiz ends """
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_button_click(self):
        """ On clicking true button check the answer and increase the score card by 1 """
        self.give_feedback(self.quiz.check_answer("True"))

    def false_button_click(self):
        """ On clicking false button check the answer and leave the score card to remain the same """
        is_correct = self.quiz.check_answer("False")
        self.give_feedback(is_correct)

    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.main_window.after(1000, self.next_question_method)
