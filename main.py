import turtle
import pandas
# creates screen
window = turtle.Screen()
window.setup(height=800, width=800)
window.title("U.S. States Game")
image = "blank_states_img.gif"
window.addshape(image)
turtle.shape(image)
# access csv
data = pandas.read_csv("50_states.csv")
# converts states column to list
all_states = data.state.to_list()
# empty list to place guessed states
guessed_states = []

while len(guessed_states) < 50:
    answer = window.textinput(title=f"{len(guessed_states)}/50 States Correct",
                              prompt="What's another state's name?").title()
    if answer == "Exit":
        missing_states = []
        # checks if state has been guessed
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer in all_states:
        # moves to state coordinates on map
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)
