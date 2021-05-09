import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")

pen = turtle.Turtle()
pen.penup()
pen.hideturtle()


def write_state(name, state_position):
    pen.goto(state_position)
    pen.write(name, align="left", font=("Arial", 8, "bold"))


all_states = states_data.state
states_list = all_states.to_list()
guessed_states = []


while len(guessed_states) != len(states_list):
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 correct", prompt="What's the state name?")
    title_case_answer = answer_state.title()
    if answer_state == "exit":
        states_to_learn_list = [state for state in states_list if state not in guessed_states]
        states_to_learn = pandas.DataFrame(states_to_learn_list)
        states_to_learn.to_csv("states_to_learn.csv")
        break
    if title_case_answer in states_list:

        selected_state = states_data[states_data.state == title_case_answer]
        selected_state_name = title_case_answer
        selected_state_x = int(selected_state.x)
        selected_state_y = int(selected_state.y)
        position = (selected_state_x, selected_state_y)
        write_state(name=selected_state_name, state_position=position)
        guessed_states.append(title_case_answer)


