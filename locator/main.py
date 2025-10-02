import time
from turtle import Turtle, Screen
from typing import Tuple

from data_handler import DataHandler

game_on = True
IMAGE_PATH = r"locator\blank_states_img.gif"
TIME = 51

states_data = DataHandler("50_states.csv")

def move_input_to(text: str, correct:bool = True):
    print(f"moving it ({text}) to: {correct}")

def check_for_str(check:str) -> None:
    low_check = check.lower()
    if low_check in states_data.data.state:
        print(f"JA!!! {low_check}")
        


def check_for(pos: list) -> int:
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
img_turtle = Turtle()
img_turtle.shape(IMAGE_PATH) # uses loaded image from screen.addshape
pos_clicked = img_turtle.onclick(get_mouse_pos)

looper = True
timer = 0
while looper:
    antwort = screen.textinput(f"Antwort {timer+1}", "Antwort")
    print(antwort.lower())
    check_for_str(antwort)
    timer += 1
    
    if timer > TIME:
        looper = False
    
screen.listen()

screen.mainloop()