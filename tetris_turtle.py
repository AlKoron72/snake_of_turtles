import turtle
import random

# Fenstergröße und Spielfeld
WINDOW_WIDTH, WINDOW_HEIGHT = 300, 600
TILE_SIZE = 30
GRID_WIDTH = WINDOW_WIDTH // TILE_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // TILE_SIZE

# Farben für die Blöcke
COLORS = ["red", "blue", "green", "yellow", "purple", "orange"]

# Tetris-Formen
SHAPES = {
    "O": [[1, 1],
          [1, 1]],
    "I": [[1],
          [1],
          [1],
          [1]],
    "T": [[1, 1, 1],
          [0, 1, 0]],
    "L": [[1, 0],
          [1, 0],
          [1, 1]],
    "Z": [[1, 1, 0],
          [0, 1, 1]]
}

# Spielfeld
grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

# Turtle-Setup
screen = turtle.Screen()
screen.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
screen.tracer(0)  # Animation deaktivieren
screen.title("Tetris mit Turtle")

# Zeichne das Spielfeld
drawer = turtle.Turtle()
drawer.hideturtle()
drawer.penup()

def draw_grid():
    drawer.clear()
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if grid[y][x]:
                drawer.goto(x * TILE_SIZE - WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - y * TILE_SIZE)
                drawer.color(grid[y][x])
                drawer.begin_fill()
                for _ in range(4):
                    drawer.forward(TILE_SIZE)
                    drawer.right(90)
                drawer.end_fill()

# Block-Klasse
class Block:
    def __init__(self):
        self.shape = random.choice(list(SHAPES.values()))
        self.color = random.choice(COLORS)
        self.x = GRID_WIDTH // 2 - len(self.shape[0]) // 2
        self.y = 0

    def draw(self):
        for row_idx, row in enumerate(self.shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    drawer.goto((self.x + col_idx) * TILE_SIZE - WINDOW_WIDTH // 2,
                                WINDOW_HEIGHT // 2 - (self.y + row_idx) * TILE_SIZE)
                    drawer.color(self.color)
                    drawer.begin_fill()
                    for _ in range(4):
                        drawer.forward(TILE_SIZE)
                        drawer.right(90)
                    drawer.end_fill()

    def move_down(self):
        self.y += 1
        if self.check_collision():
            self.y -= 1
            self.lock()
            return False
        return True

    def move_left(self):
        self.x -= 1
        if self.check_collision():
            self.x += 1

    def move_right(self):
        self.x += 1
        if self.check_collision():
            self.x -= 1

    def rotate(self):
        self.shape = list(zip(*self.shape[::-1]))
        if self.check_collision():
            self.shape = list(zip(*self.shape))[::-1]  # Rückgängig machen

    def check_collision(self):
        for row_idx, row in enumerate(self.shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    new_x = self.x + col_idx
                    new_y = self.y + row_idx
                    if new_x < 0 or new_x >= GRID_WIDTH or new_y >= GRID_HEIGHT or grid[new_y][new_x]:
                        return True
        return False

    def lock(self):
        for row_idx, row in enumerate(self.shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    grid[self.y + row_idx][self.x + col_idx] = self.color
        clear_lines()
        spawn_new_block()

# Zeilen löschen
def clear_lines():
    global grid
    new_grid = [row for row in grid if any(cell == 0 for cell in row)]
    cleared_lines = GRID_HEIGHT - len(new_grid)
    grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(cleared_lines)] + new_grid

# Neues Block-Objekt
current_block = Block()

def spawn_new_block():
    global current_block
    current_block = Block()
    if current_block.check_collision():
        print("Game Over!")
        screen.bye()

# Steuerung
def move_left():
    current_block.move_left()

def move_right():
    current_block.move_right()

def rotate():
    current_block.rotate()

def drop():
    if not current_block.move_down():
        spawn_new_block()

# Tastenbindung
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(rotate, "Up")
screen.onkeypress(drop, "Down")

# Hauptspielschleife
def game_loop():
    if current_block.move_down():
        draw_grid()
        current_block.draw()
        screen.update()
        screen.ontimer(game_loop, 500)
    else:
        spawn_new_block()

# Spiel starten
game_loop()
screen.mainloop()