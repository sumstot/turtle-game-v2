import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")
screen.onkey(player.move_right, "Right")
screen.onkey(player.move_left, "Left")

game_is_on = True

car = CarManager()
scoreboard = Scoreboard()

while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard
    car.make_car()
    car.move_car()

    for new_car in car.all_cars:
        if player.distance(new_car) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.ycor() > 290:
        player.level_up()
        scoreboard.update_level()
        car.speed_up()

screen.exitonclick()