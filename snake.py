from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.make_square([0, 0])
        self.make_square([-20, 0])
        self.make_square([-40, 0])
        self.head = self.segments[0]
        self.tail = self.segments[len(self.segments)-1]

    def make_square(self, coords):
        new_square = Turtle(shape="square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(coords)
        new_square.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.segments.append(new_square)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def extend(self):
        self.make_square(self.segments[-1].position())

    def t_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def t_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def t_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def t_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def check_lose(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True

