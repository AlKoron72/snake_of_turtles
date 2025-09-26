from flask import Flask, jsonify, request, render_template
from snake import Snake
from snake.food import Food
from score import Score

app = Flask(__name__)

# Spielfeld- und Segmentgrößen
SEGMENT_SIZE = 20
FIELD_SIZE = SEGMENT_SIZE * 30

# Spielobjekte
my_snake = Snake(SEGMENT_SIZE)
my_food = Food(segment_size=SEGMENT_SIZE, field_size=FIELD_SIZE)
my_score = Score()

@app.route("/")
def index():
    """Render die HTML-Seite für das Spiel."""
    return render_template("index.html")

@app.route("/game_state", methods=["GET"])
def get_game_state():
    """Gibt den aktuellen Spielzustand zurück."""
    snake_body = [{"x": segment.xcor(), "y": segment.ycor()} for segment in my_snake.segments]
    food_position = {"x": my_food.pos[0], "y": my_food.pos[1]}
    score = my_score.get_score()
    return jsonify({"snake": snake_body, "food": food_position, "score": score})

@app.route("/move", methods=["POST"])
def move_snake():
    """Bewegt die Schlange basierend auf der Richtung."""
    direction = request.json.get("direction")
    my_snake.turn(direction)
    snake_head_pos = my_snake.move()

    # Überprüfen, ob die Schlange das Essen erreicht hat
    if my_snake.head.distance(my_food) < 15:
        my_food.eat()
        my_snake.grow()
        my_score.increase_score()

    # Rückgabe des neuen Spielzustands
    return get_game_state()

if __name__ == "__main__":
    app.run(debug=True)