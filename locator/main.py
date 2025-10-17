#import time
#from data_handler import DataHandler
from turtle import Turtle, Screen
from typing import Tuple
import pandas as pd

game_on = True
misses = 0
IMAGE_PATH = "blank_states_img.gif"
CSV_PATH = "50_states.csv"
TIME = 50
FONT = ("Arial", 12, "bold")
ALIGN = "center"

#from data_handler import DataHandler
#data_oop = DataHandler(CSV_PATH)
#print(data_oop.data.state)

def end_result():
    print(f"end result: {misses}")

def load_from_csv(source: str):
    print(f"SOURCE: {source}")
    try:
        return pd.read_csv(source)
    except FileNotFoundError:
        print("File not found.")
        print("Please check the file path.")
        print(f"Your provided file path: {source}")

states_data = load_from_csv(CSV_PATH)
states_list = states_data.state.to_list()
missed_list = states_list.copy()

def move_input_to(text: str, correct:bool = True):
    print(f"moving it ({text}) to: {correct}")

def place_right(text:str) -> None:
    print(f"Placing -> {text}")
    for_koords = states_data[text == states_data.state]
    
    x_pos = int(for_koords.iloc[0].x)
    y_pos = int(for_koords.iloc[0].y)
#    x_pos = for_koords.x
#    y_pos = for_koords.y
    print(f"at: {x_pos}/{y_pos}")
    turd = Turtle()
    turd.pencolor("green")
    turd.goto(x_pos, y_pos)
    turd.clear()
    turd.write(text, font=FONT, align=ALIGN)
    

def check_for_str_in_list(check:str):
    if check in states_list:
        print("YO List") 
    else:
        print("list NO!!!")
        #misses += 1
    
def check_for_str(check:str) -> None:
    low_check = check.lower()
    #print(states_data.state)
    
    for state in states_data.state:
        #print(f"{state}/{check}")
        if low_check == state.lower():
            print(f"JA!!! {low_check}")
            place_right(state)
            missed_list.remove(state)
        else:
            print(f"nö: {check}")    


def check_for(pos: list) -> int:
    x = states_data.data.x
    y = states_data.data.y
    state = states_data.data.state

    if pos in states_data.data.state:
        state = states_data.data.state[pos]

    print(f"state: {state} onomatopoeia: {x}/{y}")
    return 42

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
#pos_clicked = img_turtle.onclick(get_mouse_pos)

#states_to_learn.csv
WRITE_PATH = "states_to_learn.csv"
def write_end():
    data_to_write = pd.DataFrame(missed_list)
    try:
        data_to_write.to_csv(WRITE_PATH)
    except Exception as e:
        print(f"unable to write {e}")

looper = True
timer = 0
while looper:
    antwort = screen.textinput(f"Antwort {timer+1}/{TIME} MISSES: {misses}", "Antwort")
    print(antwort.lower())
    check_for_str(antwort)
    check_for_str_in_list(antwort)
    timer += 1
    
    if timer >= TIME or antwort.lower() == "stop":
        write_end()
        looper = False
    
