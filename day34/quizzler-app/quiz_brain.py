import html


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        question_text = html.unescape(self.current_question.text) # un escape html entity eg. double quote, single quote

        # user_answer = input(f"Q.{self.question_number}: {question_text} (True/False): ")
        # self.check_answer(user_answer)
        """ using return for storing the output i.e. q.no: question text """
        return f"Q.{self.question_number}: {question_text}"

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            # print("You got it right!")
            return True
        else:
            # print("That's wrong.")
            return False

        """ Commenting out the below lines as we are storing the return values of check answer fn () """
        # print(f"Your current score is: {self.score}/{self.question_number}")
        # print("\n")