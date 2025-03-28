from turtle import Turtle
import random

# Food class is a subclass of Turtle class
class Food(Turtle):

    # Constructor of Food class
    def __init__(self):
        super().__init__()
        # Shape of the food is a circle
        self.shape("circle")
        # Penup is used to prevent the food from leaving a trail
        self.penup()
        # Shapesize is used to change the size of the food
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        # Color of the food is chartreuse
        self.color("chartreuse")
        # Speed of the food is fastest
        self.speed("fastest")
        # Refresh the food
        self.refresh()

    # Refresh the food
    def refresh(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(x=random_x, y=random_y)

    # Reset the food
    def reset_food(self):
        self.goto(1000,1000)
