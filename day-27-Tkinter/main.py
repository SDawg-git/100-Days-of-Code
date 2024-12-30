from tkinter import *


def calculate_button():
    miles = int(entry.get())
    km = miles * 1.609
    label_converted["text"] = km

window = Tk()

window.title("Mile to Km Converter")
window.minsize(width=200, height=200)
window.config(padx = 50, pady=50)       #padding

label_equal = Label(text = "is equal to ")
label_equal.grid(column = 0, row = 1)

label_miles = Label(text = "Miles")
label_miles.grid(column = 2, row = 0)

label_km = Label(text = "Km")
label_km.grid(column = 2, row = 1)

label_converted = Label(text = 0)
label_converted.grid(column = 1, row = 1)

calculate = Button(text = "Calculate", command = calculate_button)
calculate.grid(column = 1, row = 2)

entry = Entry()
entry.grid(column = 1, row = 0)







window.mainloop()
