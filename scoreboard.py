from turtle import Turtle
FONT = ("Courier", 24, "bold")
GAME_OVER = ("Courier", 72, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.setposition(-280, 270)
        self.color("black")
        self.write(f"Level: {self.level}", font=FONT)

    def update_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", font=FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write(f"GAME OVER.", align="center", font=GAME_OVER)
