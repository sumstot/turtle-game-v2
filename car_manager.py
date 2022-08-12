from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def make_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shape("square")
            new_car.turtlesize(stretch_len=random.randint(1, 3), stretch_wid=1)
            new_car.color(random.choice(COLORS))
            new_car.setposition(x=260, y=random.randint(-280, 280))
            self.all_cars.append(new_car)

    def speed_up(self):
        self.speed += MOVE_INCREMENT

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.speed)
