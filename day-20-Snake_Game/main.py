import time
from food import Food
from turtle import Screen
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")




game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)


    snake.move()

    #detect collision

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.update_score()
        snake.create_snake(1)

    #detect collision with wall:

    if snake.head.xcor() == 300 or snake.head.xcor() == -300 or snake.head.ycor() == 300 or snake.head.ycor() == -300:
        #game_over = True
        scoreboard.reset_scoreboard()
        snake.reset_snake()


    #detect collision with tail

    for turtle in snake.turtles[1:]:
        # if turtle == snake.head:
        #     pass
        if snake.head.distance(turtle) < 10:
            #game_over = True
            #scoreboard.game_over_func()

            scoreboard.reset_scoreboard()
            snake.reset_snake()


screen.exitonclick()
