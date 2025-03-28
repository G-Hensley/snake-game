from turtle import Screen
import time
from snake import Snake
from scoreboard import Scoreboard
from food import Food
FONT = ("Eccentric Std", 16, 'normal')
ALIGNMENT = "center"

# Create the screen and configure it
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Run the game
def run_game():
    # Create the snake
    snake = Snake()
    # Create the food
    food = Food()
    # Create the scoreboard
    score_board = Scoreboard()

    # Listen for key presses
    screen.listen()
    screen.onkeypress(key="Up", fun=snake.up)
    screen.onkeypress(key="Down", fun=snake.down)
    screen.onkeypress(key="Left", fun=snake.left)
    screen.onkeypress(key="Right", fun=snake.right)

    # Game loop
    game_on = True
    while game_on:
        # update the screen
        screen.update()
        # wait for 0.1 seconds
        time.sleep(0.1)
        # move the snake
        snake.move()

        # Check if the snake has eaten the food
        if snake.head.distance(food) < 15:
            snake.extend()
            food.refresh()
            score_board.score += 1
            score_board.update_score()

        # Check if the snake has hit the edge of the screen
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
            score_board.reset_screen()
            snake.reset_snake()
            food.reset_food()
            game_on = False

        # Check if the snake has hit itself
        for segment in snake.snake_list[1::]:
            if snake.head.distance(segment) < 10:
                score_board.reset_screen()
                snake.reset_snake()
                food.reset_food()
                game_on = False

    # Ask the player if they want to play again
    play_again = screen.textinput("Play Again?", "Would you like to play again? Type 'y' for Yes or 'n' for No: ").lower()
    if play_again == 'y':
        score_board.reset_screen()
        run_game()
        screen.exitonclick()
    else:
        screen.bye()

# Run the game
run_game()
