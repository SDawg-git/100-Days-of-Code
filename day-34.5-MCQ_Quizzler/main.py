from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

age = 12         #standard way of initialising variables
age2 : int       #you initialise a variable as a certain data type, and in the future when changing the data types have to match

def police_check(age:int) -> bool:      #you can check it within function inputs too, arrow indicates the expected output data type
    pass



question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
