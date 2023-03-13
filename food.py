from turtle import Turtle
import random


class Food:

    def __init__(self):
        self.all_food = []
        self.stage = 0

    def make_food(self, snake_segments, game_time, stage):
        food = Turtle()
        food.shapesize(stretch_len=0.5, stretch_wid=0.5)
        food.color("blue")
        food.speed("fastest")
        food.shape("square")
        food.penup()

        food.die_time = game_time + 12 - stage
        possible_x_coords = list(range(-280, 280, 20))
        possible_y_coords = list(range(-280, 280, 20))

        try:
            for seg in snake_segments:
                seg_x = int(round(seg.xcor(), 0))
                seg_y = int(round(seg.ycor(), 0))
                if seg_x in possible_x_coords and seg_y in possible_y_coords:
                    possible_x_coords.remove(seg_x)
                    possible_y_coords.remove(seg_y)
        except ValueError:
            x_snake_coords = [int(round(seg.xcor(), 0)) for seg in snake_segments]
            y_snake_coords = [int(round(seg.ycor(), 0)) for seg in snake_segments]

        random_x = random.choice(possible_x_coords)
        random_y = random.choice(possible_y_coords)
        food.goto(random_x, random_y)
        self.all_food.append(food)

    def delete_food(self, food_to_delete):
        food_to_delete.hideturtle()
        try:
            self.all_food.remove(food_to_delete)
        except ValueError:
            pass


