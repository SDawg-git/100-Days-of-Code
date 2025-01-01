import json
import random
from tkinter import messagebox
from tkinter import *
import random

import pyperclip            #allows to copy into clipboard



# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def random_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    #for char in range(nr_letters):
    # password_list.append(random.choice(letters))

    password_letters = [random.choice(letters) for char in range(nr_letters)]

    #for char in range(nr_symbols):
    #  password_list += random.choice(symbols)
    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]


    #for char in range(nr_numbers):
    #  password_list += random.choice(numbers)
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]

    all_lists = password_letters + password_numbers + password_symbols

    random.shuffle(all_lists)

    password = ""
    for char in all_lists:
      password += char

    password_entry.delete(0, END)
    password_entry.insert(END, string=password)
    pyperclip.copy(password)




# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():

    website_data = website_entry.get()
    email_data = email_entry.get()
    password_data = password_entry.get()
    new_data = {
        website_data: {
            "email": email_data,
            "password": password_data,
        }
    }

    if website_data == "" or email_data == "" or password_data == "":
        messagebox.showinfo(title="Missing info", message="Please fill in all the blanks.")
    else:
        #is_ok = messagebox.askokcancel(title=website_data, message=f"These are the details entered: \nEmail: {email_data} \nPassword: {password_data}\nIs this correct?")
        #if is_ok:                          #this was removed in lesson 30

        try:
            with open("not passwords.json", "r") as file:
                #file.write(f"\n{website_data} | {email_data} | {password_data}")
                #json.dump(new_data, file, indent=4)                                 #writing / overwriting data
                #data = json.load(file)                                             # #loading data

                data = json.load(file)
                data.update(new_data)                                                #have to grab current data, update the data you wanna throw in, then write

            with open("not passwords.json", "w") as file:

                json.dump(data, file, indent=4)


        except FileNotFoundError:
            print("File not found, creating file...")
            with open("not passwords.json", "w") as file:
                json.dump(new_data, file, indent=4)

        else:
            website_entry.delete(0, END)
            password_entry.delete(0, END)



def success_popup():
    pass

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")

canvas = Canvas(height=200, width=200)
bg_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=bg_image)
canvas.grid(column=1,row=0)


website_entry = Entry(width=39)
website_entry.insert(END, string="")
#Gets text in entry
#print(entry.get())
website_entry.grid(column=1, row=1, columnspan = 2)                 #columnspan is used to put a single widget over several columns
website_entry.focus()


email_entry = Entry(width=39)
email_entry.insert(END, string="dzemojad2002@gmail.com")
email_entry.grid(column=1, row=2, columnspan = 2)

password_entry = Entry(width=21)
password_entry.insert(END, string="")
password_entry.grid(column=1, row=3)


website_label = Label(text="Website:")
website_label.grid(column = 0, row = 1)

email_label = Label(text="Email/Username:")
email_label.grid(column = 0, row = 2)

password_label = Label(text="Password:")
password_label.grid(column = 0, row = 3)


password_button = Button(text="Generate Password", command=random_password)
password_button.grid(column = 2, row = 3)

submit_button = Button(text="Add", width=36, command = save_data)
submit_button.grid(column=1, row = 4, columnspan=2)

def find_website():
    website = website_entry.get()

    with open("not passwords.json", "r") as file:
        data_dict = json.load(file)

        try:
            website_mail = data_dict[website]["email"]
            website_pass = data_dict[website]["password"]
            messagebox.showinfo(website, message=f"Email: {website_mail}\n Password: {website_pass}")

        except KeyError as error:
            messagebox.showinfo("Error", message=f"No credentials for website {error}")

        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found")




search_button = Button(text="Search", command=find_website)
search_button.grid(column=3, row=1)




window.mainloop()
