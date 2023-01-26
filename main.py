import turtle
import pandas as pd

screen = turtle.Screen()
screen.setup(width=1410, height=755)
screen.title("TR City Game")
image = "tr-map.gif"
screen.addshape(image)
turtle.shape(image)

df = pd.DataFrame({"Ankara": [-197, 127], "Eskişehir": [-318, 112], "İstanbul": [-476, 263]})
df = df.T
df.columns = ["x", "y"]
guessed_states = []

while len(guessed_states) < 81:
    answer_state = screen.textinput(title= f"{len(guessed_states)}/50 States Correct", prompt="What's another city name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in df.index if state not in guessed_states]
        print(missing_states)
        # new_data = pd.DataFrame(missing_states)
        # new_data.to_csv("states_to_learn.csv")

        break

    if answer_state in df.index:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(df.loc[answer_state, "x"], df.loc[answer_state, "y"])
        t.write(answer_state, align="center", font=("Arial", 10, "bold"))



# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)

