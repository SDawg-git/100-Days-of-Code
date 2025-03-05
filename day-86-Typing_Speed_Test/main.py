import tkinter as tk
import time


text_messages = [
    "Ten years after graduating from business school, a group of alumni gathered for their reunion.",
    "As they reminisced about their college days and shared stories of their careers, a common theme emerged: the power of networking.",
    "Many of them had landed their first jobs through connections made in school.",
    "Others had collaborated on successful business ventures with former classmates.",
    "One alumnus, Emily, had even met her husband through a mutual friend from the program.",
    "The reunion served as a reminder of the importance of building and maintaining relationships throughout one's career.",
    "It highlighted the value of staying connected with former colleagues, mentors, and classmates, who could offer support, advice, and opportunities.",
    "The alumni resolved to stay in touch more regularly, recognizing that their network was a valuable asset that could help them in the future."
]

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Speed Typing Test")

        #UI

        self.sentence_display = tk.Text(root, height=3, width=80, font=("Arial", 14), wrap="word", state="disabled")
        self.sentence_display.pack(pady=10)

        self.entry = tk.Entry(root, font=("Arial", 14), width=80)
        self.entry.pack(pady=10)
        self.entry.bind("<KeyRelease>", self.check_input)  #Checks input as its typed, highlights letter 

        self.feedback_label = tk.Label(root, text="", font=("Arial", 12), fg="red")
        self.feedback_label.pack(pady=5)

        self.start_button = tk.Button(root, text="Start", font=("Arial", 14), command=self.start_test)
        self.start_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 14), fg="green")
        self.result_label.pack(pady=10)


        #variables
        self.current_sentence_index = 0
        self.start_time = None
        self.total_words = 0

    def start_test(self):
        self.current_sentence_index = 0
        self.total_words = 0
        self.result_label.config(text="")
        self.start_time = time.time()           #starts timer
        self.show_sentence()
        self.entry.delete(0, tk.END)
        self.entry.focus()

    def show_sentence(self):                            #displays current sentence
        self.sentence_display.config(state="normal")
        self.sentence_display.delete("1.0", tk.END)
        self.sentence_display.insert(tk.END, text_messages[self.current_sentence_index])
        self.sentence_display.config(state="disabled")

    def check_input(self, event=None):
        user_text = self.entry.get()
        correct_text = text_messages[self.current_sentence_index]


        self.sentence_display.config(state="normal")
        self.sentence_display.delete("1.0", tk.END)
        self.sentence_display.insert(tk.END, correct_text)
        self.sentence_display.tag_remove("correct", "1.0", tk.END)
        self.sentence_display.tag_remove("wrong", "1.0", tk.END)

        for i in range(len(user_text)):                             #checks if current letter matches the sentence
            if i < len(correct_text):
                tag = "correct" if user_text[i] == correct_text[i] else "wrong"
                self.sentence_display.tag_add(tag, f"1.{i}", f"1.{i+1}")


        self.sentence_display.tag_config("correct", foreground="green")
        self.sentence_display.tag_config("wrong", foreground="red")

        self.sentence_display.config(state="disabled")                  #locks text box


        if user_text == correct_text:                                       #checks if sentences match
            self.total_words += len(correct_text.split())  #counts words for WPM calculation
            self.current_sentence_index += 1  #moves to next sentence
            self.entry.delete(0, tk.END)


            if self.current_sentence_index < len(text_messages):
                self.show_sentence()
            else:
                self.end_test()

    def end_test(self):
        end_time = time.time()
        time_taken = end_time - self.start_time  #time in seconds
        minutes = time_taken / 60
        wpm = self.total_words / minutes if minutes > 0 else 0

        self.result_label.config(text=f"Test Complete! Your speed: {wpm:.2f} WPM")
        self.feedback_label.config(text="")
        self.sentence_display.config(state="normal")
        self.sentence_display.delete("1.0", tk.END)
        self.sentence_display.insert(tk.END, "Test Complete! Click 'Start' to try again.")
        self.sentence_display.config(state="disabled")



root = tk.Tk()
typing_test = TypingSpeedTest(root)
root.mainloop()
