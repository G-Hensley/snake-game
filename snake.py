from turtle import Turtle

COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

# The snake class controls the snake's movement and the snake's segments
class Snake:

    # Constructor of the snake class
    def __init__(self):
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]

    # Create the snake
    def create_snake(self):
        for pos in COORDINATES:
            self.add_segment(pos)

    # Add a segment to the snake
    def add_segment(self, position):
        new_snake = Turtle("square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        self.snake_list.append(new_snake)

    # Extend the snake
    def extend(self):
        self.add_segment(self.snake_list[-1].position())

    # Move the snake
    def move(self):
        for section in range(len(self.snake_list) - 1, 0, -1):
            new_x = self.snake_list[section - 1].xcor()
            new_y = self.snake_list[section - 1].ycor()
            self.snake_list[section].goto(new_x, new_y)
        self.snake_list[0].forward(MOVE_DISTANCE)

    # Move the snake up
    def up(self):
        if self.head.heading() != DOWN:
            self.snake_list[0].setheading(UP)

    # Move the snake down
    def down(self):
        if self.head.heading() != UP:
            self.snake_list[0].setheading(DOWN)

    # Move the snake right
    def right(self):
        if self.head.heading() != LEFT:
            self.snake_list[0].setheading(RIGHT)

    # Move the snake left
    def left(self):
        if self.head.heading() != RIGHT:
            self.snake_list[0].setheading(LEFT)

    # Reset the snake
    def reset_snake(self):
        for segment in self.snake_list:
            segment.goto(1000,1000)

