import time
from turtle import Turtle, Screen
from typing import Tuple

from locator.data_handler import DataHandler

game_on = True
IMAGE_PATH = "blank_states_img.gif"

states_data = DataHandler("50_states.csv")

def check_for(pos: list,) -> int:
    x = states_data.data.x
    y = states_data.data.y
    state = states_data.data.state

    if pos in states_data.data.state:
        state = states_data.data.state[pos]

def get_mouse_pos(x: float, y: float) -> Tuple[float, float]:
    print(f"Mouse clicked at ({x}, {y})")
    return x, y

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")
screen.title("Locator-Game")
screen.addshape(IMAGE_PATH) # load image for turtle later
antwort = screen.textinput("Antwort", "Antwort")
#screen.tracer(0)
#screen.listen()

img_turtle = Turtle()
img_turtle.shape(IMAGE_PATH) # uses loaded image from screen.addshape
pos_clicked = img_turtle.onclick(get_mouse_pos)
screen.listen()

screen.mainloop()