from tkinter import *
from tkinter import Canvas
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface():

    def __init__(self, quiz_brain: QuizBrain):



        self.score = 0
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)
        self.window.minsize(width=300, height=350)

        self.score_label = Label(text=f"Score: {self.score}", bg=THEME_COLOR, font=("Arial", 10, "italic"), foreground="white")
        #self.score_label.config(padx=20, pady=20)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Question text", fill=THEME_COLOR, font=("Arial", 20, "italic"),  width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)



        tick_image = PhotoImage(file="images/true.png")
        self.tick_button = Button(image=tick_image,highlightthickness=0, command=self.true_button)
        self.tick_button.grid(column=1, row = 2)

        cross_image = PhotoImage(file="images/false.png")
        self.cross_button = Button(image=cross_image,highlightthickness=0, command= self.false_button)
        self.cross_button.grid(column=0, row = 2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q_text)
            #next_q = QuizBrain.next_question(self.quiz)                 #I was right this does work
            #self.canvas.itemconfig(self.question_text, text=next_q)
        else:
            self.canvas.itemconfig(self.question_text, text = "You've reached the end of the quiz")
            self.tick_button.config(state="disabled")
            self.cross_button.config(state="disabled")

    def true_button(self):
        #is_right = self.quiz.check_answer("True")
        self.give_feedback(self.quiz.check_answer("True"))


    def false_button(self):
        #is_right = self.quiz.check_answer("False")
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
            self.score +=1
            self.score_label.config(text=f"Score: {self.score}", bg=THEME_COLOR, font=("Arial", 10, "italic"), foreground="white")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)

