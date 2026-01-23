import time
import turtle as t

from src.snake import Snake
from src.food import Food
from src.scoreboard import Scoreboard

LIMIT = 290

# setup screen dimensions and color
screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        score.increase_score()
        food.refresh()

    #Detect collision with wall
    if snake.head.xcor() > LIMIT or snake.head.xcor() < -LIMIT or snake.head.ycor() > LIMIT or snake.head.ycor() < -LIMIT:
        game_is_on = False
        score.game_over()

screen.mainloop()