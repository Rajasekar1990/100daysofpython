class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.user_answer = ""
        self.correct_answer = ""
        self.score = 0

    def next_question(self):
        question_asked = self.question_list[self.question_number]
        self.question_number += 1
        self.user_answer = input(f"Q.{self.question_number} {question_asked.text} (True/False): ").lower()
        self.correct_answer = question_asked.answer

    def still_has_question(self):
        len(self.question_list)
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def check_answer(self):
        if self.user_answer.lower() == self.correct_answer.lower():
            self.score += 1
            print("You are right")
        else:
            print("You are wrong")
        print(f"the correct answer was {self.correct_answer.lower()}")
        print(f"your current score is {self.score}\n")

    def final_score(self):
        print("You've completed the quiz")
        print(f"Your final score was {self.score}/{len(self.question_list)}")
