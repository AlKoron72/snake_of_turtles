from turtle import Screen

def setup_screen(field_size, turn_callback, title="Pong Game", bg_color="black"):
    screen = Screen()
    screen.setup(width=field_size[0], height=field_size[1])
    screen.title(title)
    screen.bgcolor(bg_color)
    screen.tracer(0)

    # Steuerung einrichten
    screen.listen()
    screen.onkey(key="Up", fun=lambda: turn_callback("up"))
    screen.onkey(key="Down", fun=lambda: turn_callback("down"))

    return screen