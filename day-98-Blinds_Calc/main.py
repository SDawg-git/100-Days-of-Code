#upload when back


# Remember to add the cost of clear rods

#make sure an invoice email is sent when done

#sort out the email perms

#create email pass to use in app

#make sure to follow the vid to package the app correctly so it can be ran as an .exe

#ADD 20% OF TOTAL COST OF BLIND PER ADDON

#dropdown list with all email addresses to send invoices to + button to add more


from tkinter import *
from tkinter import ttk
from tkinter import messagebox

BG_COLOR = "#B9E5E8"

window = Tk()

window.title("Cost Calculator")
window.minsize(width=300, height=500)
label = Label(text="SW General Tailoring Cost Calculator", font=("Monospace", 20), bg=BG_COLOR)
label.grid(column = 1, row = 0)
window.config(background=BG_COLOR)

blinds = [
    "Blackout",
    "something else"
]

cost_dict = {
    "Blackout": 90,
    "Lined/Interlined" : 85,
    "Unlined/Sheer" : 70,
}


# def listbox_used(event):
#     # Gets current selection from listbox
#     print(dropdown_menu.get(dropdown_menu.curselection()))

dropdown_menu = Listbox(height=3)
blinds = ["Blackout", "Lined/Interlined", "Unlined/Sheer"]
for item in blinds:
    dropdown_menu.insert(blinds.index(item), item)
#dropdown_menu.bind("<<ListboxSelect>>", listbox_used)
dropdown_menu.place(x=175, y=50)

type_label = Label(text="Type:", bg=BG_COLOR)
type_label.place(x=120, y=50)

height_label = Label(text="Height (in meters):", bg=BG_COLOR)
height_label.place(x=50, y=125)

height_entry = Entry(width=20)
height_entry.place(x=175, y=125)

width_label = Label(text="Width (in meters):", bg=BG_COLOR)
width_label.place(x=50, y=150)

width_entry = Entry(width=20)
width_entry.place(x=175, y=150)

extras_label = Label(text="Extras:", bg=BG_COLOR)
extras_label.place(x=90, y=190)

# #Checkbutton
# def checkbutton_used():
#     #Prints 1 if On button checked, otherwise 0.
#     print(velcro_checked_state.get())
# #variable to hold on to checked state, 0 is off, 1 is on.
velcro_checked_state = IntVar()
velcro_checkbutton = Checkbutton(text="Velcro", variable=velcro_checked_state, background=BG_COLOR)  #command=checkbutton_used,
velcro_checked_state.get()
velcro_checkbutton.place(x=150, y=180)

other_checked_state = IntVar()
other_checkbutton = Checkbutton(text="Other", variable=other_checked_state, background=BG_COLOR)        ## FIX THESE NAMES THEN ADD TO THE COST CALCULATOR
other_checked_state.get()
other_checkbutton.place(x=150, y=200)

another_checked_state = IntVar()
another_checkbutton = Checkbutton(text="Another", variable=another_checked_state, background=BG_COLOR)
another_checked_state.get()
another_checkbutton.place(x=215, y=200)



def get_cost():
    cost = 0

    blind_type = dropdown_menu.get(dropdown_menu.curselection())
    blind_cost = cost_dict[blind_type]

    if velcro_checked_state.get() == 1:
        #cost += ("WHATEVER VELCRO COST IS, DO THE SAME FOR OTHER BUTTONS")
        pass

    blind_width = float(width_entry.get())
    blind_height = float(height_entry.get())
    size = round(float(blind_width) * float(blind_height), 3)            #rounds to 3dp
    cost += size * blind_cost

    print(size)
    print(blind_cost)




    messagebox.showinfo("cost", message=f"£{cost}")

calculate_button = Button(text="Calculate", font=("Arial", 10), command=get_cost)
calculate_button.place(x=200, y=400)





window.mainloop()
