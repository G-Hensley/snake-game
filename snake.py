from turtle import Turtle

COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]

    def create_snake(self):
        for pos in COORDINATES:
            self.add_segment(pos)

    def add_segment(self, position):
        new_snake = Turtle("square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        self.snake_list.append(new_snake)

    def extend(self):
        self.add_segment(self.snake_list[-1].position())

    def move(self):
        for section in range(len(self.snake_list) - 1, 0, -1):
            new_x = self.snake_list[section - 1].xcor()
            new_y = self.snake_list[section - 1].ycor()
            self.snake_list[section].goto(new_x, new_y)
        self.snake_list[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.snake_list[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.snake_list[0].setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.snake_list[0].setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.snake_list[0].setheading(LEFT)

    def reset_snake(self):
        for segment in self.snake_list:
            segment.goto(1000,1000)

