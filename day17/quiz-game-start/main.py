from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    item_key = item["text"]
    item_value = item["answer"]
    question_object = Question(item_key, item_value)
    question_bank.append(question_object)

quiz_object = QuizBrain(question_bank)
# score = 0
# for j in range(1, len(question_bank)):
#     quiz_object.next_question()
#     if question_object.answer.lower() == quiz_object.user_answer:
#         score += 1
#         print("You got it right")
#         print(f"The correct answer is: {question_object.answer}")
#         print(f"Your Current score is {score}\n")
#
#     else:
#         print("That's Wrong")
#         print(f"The correct answer is: {question_object.answer}")
#         print(f"Your Current score is {score}\n")

while quiz_object.still_has_question():
    quiz_object.next_question()
    quiz_object.check_answer()

# quiz_object.final_score()
print("You've completed the quiz")
print(f"Your final score was {quiz_object.score}/{len(quiz_object.question_list)}")
