import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
screen.setup(width=725, height=491)


data_file = pandas.read_csv("50_states.csv")
state_names = data_file["state"].to_list()


game_over = False
states_correct = 0
guessed_states = []

while not game_over:

    answer_state = screen.textinput(title=f"{states_correct}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state in state_names:
        #print("Bazinga")
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)
            states_correct+=1
            new_turtle = turtle.Turtle()
            new_turtle.hideturtle()
            new_turtle.penup()

            current_state = data_file[data_file["state"] == answer_state]
            current_state_x = int(current_state.x)
            current_state_y = int(current_state.y)
            #print(current_state_x, current_state_y)
            new_turtle.goto(current_state_x, current_state_y)
            new_turtle.write(answer_state)

    elif answer_state == "Exit" or states_correct == 50:
        game_over = True

        states_to_learn = state_names
        for state in state_names:
            if state in guessed_states:
                states_to_learn.remove(state)

        states_to_learn_panda = pandas.DataFrame(states_to_learn)
        states_to_learn_panda.to_csv("states_to_learn")



#states to learn.csv




#turtle.mainloop()        #keeps screen open just like exit on click
