from turtle import Turtle

# Scoreboard class is a subclass of Turtle class
class Scoreboard(Turtle):

    # Constructor of Scoreboard class
    def __init__(self):
        super().__init__()
        # Hide the turtle
        self.hideturtle()
        # Color of the scoreboard is chartreuse
        self.color("chartreuse")
        # Speed of the scoreboard is fastest
        self.speed("fastest")
        # Penup is used to prevent the scoreboard from leaving a trail
        self.penup()
        # Go to the position (0, 270)
        self.goto(x=0, y=270)
        # Score of the scoreboard is 0
        self.score = 0
        # Read the high score from the file
        with open("snake_game_score.txt") as score_file:
            self.high_score = int(score_file.read())
        # Update the score
        self.update_score()

    # Game over function
    def game_over(self):
        # Go to the position (0, 0)
        self.goto(x=0, y=0)
        # Write the game over message
        self.write(arg="Game Over.", align="center", font=("ArcadeClassic", 20, 'normal'))

    # Update the score
    def update_score(self):
        # Clear the screen
        self.clear()
        # Write the score
        self.write(arg=f"Score: {self.score}   High Score: {self.high_score}", align='center',
                   font=("ArcadeClassic", 20, 'normal'))

    # Reset the screen
    def reset_screen(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("snake_game_score.txt", mode='w') as file:
            file.write(str(self.high_score))
        self.score = 0
        self.clear()
