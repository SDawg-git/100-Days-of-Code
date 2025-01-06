from tkinter import *
from tkinter import Canvas
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"



class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):



        self.score = 0
        self.quiz = quiz_brain
        self.user_answer = self.radio_used
        self.radio_buttons = []


        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)
        self.window.minsize(width=300, height=575)

        self.score_label = Label(text=f"Score: {self.score}", bg=THEME_COLOR, font=("Arial", 10, "italic"), foreground="white")
        #self.score_label.config(padx=20, pady=20)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Question text", fill=THEME_COLOR, font=("Arial", 20, "italic"),  width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)




        self.get_next_question()

        #print(f"Answer list: {self.quiz.answer_list}")      #USE ANSWER LIST SOMEWHERE
        #print(self.quiz.answer_list[0])

        #print(self.quiz.q_answer)         #ALSO HAVE FREE USE OF THE CORRECT ANSWER
        #NOW SORT THEM IN A RANDOM ORDER (IMPORT RANDOM), THEN PUT THEM INTO EACH OF THE RADIO BUTTONS AND UPDATE THE CHECKING FUNCTION
        #WRITE A FUNCTION THAT UPDATES THE RADIOBUTTONS WITH NEW QUESTION DATA IMMEDIATELY AFTER PROGRAM IS RAN

        self.radio_state = StringVar()
        self.radiobutton_option1 = Radiobutton(text=self.quiz.answer_list[0], value=self.quiz.answer_list[0], variable=self.radio_state, command=self.radio_used, font=("Arial", 10, "bold"))
        self.radiobutton_option1.place(x=25, y=350)

        self.radiobutton_option2 = Radiobutton(text=self.quiz.answer_list[1], value=self.quiz.answer_list[1], variable=self.radio_state, command=self.radio_used, font=("Arial", 10, "bold"))
        self.radiobutton_option2.place(x=25, y=400)

        self.radiobutton_option3 = Radiobutton(text=self.quiz.answer_list[2], value=self.quiz.answer_list[2], variable=self.radio_state, command=self.radio_used, font=("Arial", 10, "bold"))
        self.radiobutton_option3.place(x=25, y=450)

        self.radiobutton_option4 = Radiobutton(text=self.quiz.answer_list[3], value=self.quiz.answer_list[3], variable=self.radio_state, command=self.radio_used, font=("Arial", 10, "bold"))
        self.radiobutton_option4.place(x=25, y=500)

        self.radio_buttons.append(self.radiobutton_option1)
        self.radio_buttons.append(self.radiobutton_option2)
        self.radio_buttons.append(self.radiobutton_option3)
        self.radio_buttons.append(self.radiobutton_option4)

        self.update_buttons()


        self.window.mainloop()


    def radio_used(self):
        self.user_answer = self.radio_state.get()
        for button in self.radio_buttons:
            button.config(state="disabled")
        #print(self.user_answer)
        self.give_feedback(self.quiz.check_answer(self.user_answer))
        self.update_buttons()


    def get_next_question(self):
        for button in self.radio_buttons:
            button.config(bg="white", state="active", disabledforeground="black")

        self.canvas.config(bg="white")
        try:
            if self.quiz.still_has_questions():
                q_text = self.quiz.next_question()
                self.canvas.itemconfig(self.question_text, text = q_text)
                #self.radiobutton_option1.config(text= self.quiz.)                                   ############           NEED TO CHANGE THE NEW ANSWERS
                #print(f"Current Question: {self.quiz.current_question.text}")
                #print(f"Current Answer list: {self.quiz.current_question.wrong_answers}")
                #print(self.quiz.answer_list)
                self.update_buttons()
            else:
                self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
                # self.tick_button.config(state="disabled")
                # self.cross_button.config(state="disabled")
        except AttributeError as error:
            #print(error)
            pass




    def update_buttons(self):
        self.radiobutton_option1.config(text=self.quiz.answer_list[0], value=self.quiz.answer_list[0])
        self.radiobutton_option2.config(text=self.quiz.answer_list[1], value=self.quiz.answer_list[1])
        self.radiobutton_option3.config(text=self.quiz.answer_list[2], value=self.quiz.answer_list[2])
        self.radiobutton_option4.config(text=self.quiz.answer_list[3], value=self.quiz.answer_list[3])




    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
            self.score +=1
            self.score_label.config(text=f"Score: {self.score}", bg=THEME_COLOR, font=("Arial", 10, "italic"), foreground="white")
        else:
            self.canvas.config(bg="red")

        for button in self.radio_buttons:
            if button["value"] == self.quiz.q_answer:
                button.config(bg = "green", disabledforeground="white")




        self.window.after(2000, self.get_next_question)

