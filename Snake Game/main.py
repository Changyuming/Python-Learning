from turtle import Turtle, Screen
from snake import Snake
from food import Food
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# for i in range(3):
#     body = Turtle(shape="square")
#     body.color("white")
#     body.goto(-20*i, 0)

snake = Snake()
food = Food()
scoreborad = Scoreboard()

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
        food.refresh()
        snake.extend()
        scoreborad.increase_score()

    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreborad.game_over()
        game_is_on = False

    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreborad.game_over()
            game_is_on = False





screen.exitonclick()