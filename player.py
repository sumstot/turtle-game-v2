from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("green")
        self.shape("turtle")
        self.setheading(90)
        self.setposition(STARTING_POSITION)
        self.showturtle()

    def move_up(self):
        self.setheading(90)
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    def move_down(self):
        self.setheading(270)
        new_y = self.ycor() - 10
        self.goto(self.xcor(), new_y)

    def move_left(self):
        self.setheading(180)
        new_x = self.xcor() - 10
        self.goto(new_x, self.ycor())

    def move_right(self):
        self.setheading(0)
        new_x = self.xcor() + 10
        self.goto(new_x, self.ycor())

    def level_up(self):
        self.hideturtle()
        self.setposition(STARTING_POSITION)
        self.showturtle()
