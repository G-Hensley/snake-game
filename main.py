from turtle import Screen
import time
from snake import Snake
from scoreboard import Scoreboard
from food import Food
FONT = ("Eccentric Std", 16, 'normal')
ALIGNMENT = "center"

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


def run_game():
    snake = Snake()
    food = Food()
    score_board = Scoreboard()

    screen.listen()
    screen.onkeypress(key="Up", fun=snake.up)
    screen.onkeypress(key="Down", fun=snake.down)
    screen.onkeypress(key="Left", fun=snake.left)
    screen.onkeypress(key="Right", fun=snake.right)
    game_on = True
    while game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        if snake.head.distance(food) < 15:
            snake.extend()
            food.refresh()
            score_board.score += 1
            score_board.update_score()

        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
            score_board.reset_screen()
            snake.reset_snake()
            food.reset_food()
            game_on = False

        for segment in snake.snake_list[1::]:
            if snake.head.distance(segment) < 10:
                score_board.reset_screen()
                snake.reset_snake()
                food.reset_food()
                game_on = False

    play_again = screen.textinput("Play Again?", "Would you like to play again? Type 'y' for Yes or 'n' for No: ").lower()
    if play_again == 'y':
        score_board.reset_screen()
        run_game()
        screen.exitonclick()
    else:
        screen.bye()


run_game()
