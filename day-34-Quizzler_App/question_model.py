class Question:

    def __init__(self, q_text, q_answer, q_wrong_answers: []):
        self.text = q_text
        self.answer = q_answer
        self.wrong_answers = q_wrong_answers
