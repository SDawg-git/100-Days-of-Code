from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface




question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    question_wrong_answers = question["incorrect_answers"]
    new_question = Question(question_text, question_answer, question_wrong_answers)
    question_bank.append(new_question)



# for question in question_bank:                    #THATS HOW YOU GET A SINGLE ITEM
#     print(question.wrong_answers)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()


