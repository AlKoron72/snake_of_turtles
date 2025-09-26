import time
from turtle import Turtle, Screen

from locator.data_handler import DataHandler

game_on = True
IMAGE_PATH = "blank_states_img.gif"

states_data = DataHandler("50_states.csv")

def check_for(text: str) -> int:
    x = states_data.data.x
    y = states_data.data.y
    state = states_data.data.state


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Locator-Game")
screen.addshape(IMAGE_PATH)
screen.tracer(0)

image_holding_turtle = Turtle()
image_holding_turtle.shape(IMAGE_PATH)

while game_on:
    screen.update()
    time.sleep(1.0)