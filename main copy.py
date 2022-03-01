import turtle
import pandas
screen = turtle.Screen()
screen.title("US-States_Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states = []
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title = f"{len(guessed_states)}/50 guessed", 
                prompt= "What's another State's name?").title()

    if answer_state == "Exit":
        break
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        data_now = data[data.state == answer_state]
        t.goto(int(data_now.x),int(data_now.y))
        t.write(answer_state)
        guessed_states.append(answer_state)

not_guessed = []
for state in all_states:
    if state not in guessed_states:
        not_guessed.append(state)

print(not_guessed)

not_guessed_csv = pandas.DataFrame(not_guessed)

not_guessed_csv.to_csv("Not_guessed_states.csv")

# print(answer_state)

