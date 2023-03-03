from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

LIMS = 290 # in-game boundaries

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

# Setup in game objects
scoreboard = Scoreboard()
timer = Scoreboard()
stage_text = Scoreboard()
snake = Snake()
food = Food()
food.make_food([], 0, 1)
screen.update()

# Make WASD keys as the snake's movement
screen.onkey(key='a', fun=snake.t_left)
screen.onkey(key='d', fun=snake.t_right)
screen.onkey(key='w', fun=snake.t_up)
screen.onkey(key='s', fun=snake.t_down)

game_is_on = True
time_left = 15  # in-game countdown timer (when it reaches 0, game is over)
run_time = 0  # overall run-time of the game 
stage = 1
stage_text.edit_stage(stage)

while game_is_on:
    screen.update()
    time.sleep(0.1)
    time_left -= 0.1
    run_time += 0.1

    snake.move()
    timer.update_timer(round(time_left, 2))

    # Make a food object every 10 seconds
    if round(run_time, 1) % 10 == 0:
        food.make_food(snake.segments, run_time, stage)

    # For each food object on screen, check if it needs to be deleted, or it needs to change color
    for a_food in food.all_food:
        if round(a_food.die_time, 1) == round(run_time, 1):
            food.delete_food(a_food)        
        if snake.head.distance(a_food) < 10:
            snake.extend()
            food.delete_food(a_food)
            food.make_food(snake.segments, run_time, stage)
            time_left += 3
            scoreboard.update_score()
            if scoreboard.score % 10 == 0 and scoreboard.score != 0:
                if stage < 5:
                    stage += 1
                    stage_text.edit_stage(stage)
        if round(a_food.die_time - run_time, 1) == 5:
            a_food.color("yellow")
        if round(a_food.die_time - run_time, 1) == 2:
            a_food.color("red")

    if snake.head.xcor() > LIMS or snake.head.xcor() < -LIMS or snake.head.ycor() > LIMS or snake.head.ycor() < -LIMS:
        game_is_on = False
        scoreboard.end_game()

    lose_check = snake.check_lose()
    if lose_check or time_left <= 0.1:
        game_is_on = False
        scoreboard.end_game()


screen.exitonclick()
