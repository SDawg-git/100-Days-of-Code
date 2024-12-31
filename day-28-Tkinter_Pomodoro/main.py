import math
from itertools import count
from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checkmark_string = ""
my_timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    global checkmark_string
    window.after_cancel(my_timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg = "Pink")
    reps = 0
    checkmark_string = ""
    check_marks.config(text=checkmark_string)

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    global checkmark_string
    reps +=1
    work_sec = WORK_MIN #* 60
    short_break_sec = SHORT_BREAK_MIN #* 60
    long_break_sec = LONG_BREAK_MIN #* 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)

    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)

    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)
        checkmark_string +="✔"




    # if reps != 8 or reps == 1 and reps % 2 != 0:
    #     count_down(work_sec)
    #     reps +=1
    # elif reps != 8 and reps % 2 == 0:
    #     count_down(short_break_sec)
    #     reps += 1
    # elif reps == 8:
    #     count_down(long_break_sec)
    #     reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):


    count_minute = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds == 0:
        count_seconds = "00"
    if int(count_seconds) < 10 and int(count_seconds) != 0:       #had to add second if statement otherwise it'd say 0:000 at the end
        count_seconds = f"0{count_seconds}"

    if count >= 0:
        global my_timer
        canvas.itemconfig(timer_text, text=f"{count_minute}:{count_seconds}")
        my_timer = window.after(1000, count_down, count-1)
    else:
        check_marks.config(text=checkmark_string)
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW,  font=(FONT_NAME,50,"bold"))
title_label.grid(column=1, row=0)



canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomate_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=tomate_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="White")
canvas.grid(column = 1, row = 1)



start_button = Button(text="Start", command=start_timer)
start_button.grid(column = 0, row = 2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column = 3, row = 2)

check_marks = Label(text=checkmark_string, fg = GREEN, bg= YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
