import html
from random import shuffle


class QuizBrain:

    def __init__(self, q_bank):
        self.question_number = 0
        self.score = 0
        self.question_list = q_bank
        self.current_question = None
        self.answer_list = []
        self.q_answer = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.answer_list.clear()
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1

        q_text = html.unescape(self.current_question.text)
        self.q_answer = html.unescape(self.current_question.answer)
        self.answer_list.append(self.q_answer)
        for wrong_answer in self.current_question.wrong_answers:
            self.answer_list.append(html.unescape(wrong_answer))
        #print(self.answer_list)
        shuffle(self.answer_list)



        # for wrong_answer in self.current_question["incorrect_answers"]:
        #     self.answer_list.append(wrong_answer)

        #answer1 = html.unescape(self.current_question)                                              ######

        return f"Q.{self.question_number}: {q_text} "
        # user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ")
        # self.check_answer(user_answer)


    def check_answer(self, user_answer):
        correct_answer = self.q_answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            #print("You got it right!")
            return True
        else:
            #print("That's wrong.")
            return False
