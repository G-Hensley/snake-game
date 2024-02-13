from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("chartreuse")
        self.speed("fastest")
        self.penup()
        self.goto(x=0, y=270)
        self.score = 0
        with open("snake_game_score.txt") as score_file:
            self.high_score = int(score_file.read())
        self.update_score()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg="Game Over.", align="center", font=("ArcadeClassic", 20, 'normal'))

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}   High Score: {self.high_score}", align='center',
                   font=("ArcadeClassic", 20, 'normal'))

    def reset_screen(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("snake_game_score.txt", mode='w') as file:
            file.write(str(self.high_score))
        self.score = 0
        self.clear()
