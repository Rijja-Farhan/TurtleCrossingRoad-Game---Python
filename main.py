import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# setting up creen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("Black")
screen.listen()
screen.tracer(0)

# turtle
my_turtle = Player()

score = Scoreboard()

# moving the turtle
screen.onkey(my_turtle.move_up, "Up")

# while the game is on keep creating cars
# keep al cars in a list and caaled move function in a loop
game_is_on = True
sleep_time=1
all_cars = []
while game_is_on:
    time.sleep(sleep_time)
    screen.update()
    my_cars = CarManager()
    all_cars.append(my_cars)
    for cars in range(10):
        my_cars.move(all_cars)
        #detecting collision with car
        if my_cars.detect(all_cars, my_turtle):
            my_turtle.write("Game over")
            game_is_on = False
            break

    # detecting the finishline
    if my_turtle.gameFininsh():
        if sleep_time - 0.2 <= 0.2:
            game_is_on = False
            my_turtle.write("Game finish")
        sleep_time = sleep_time - 0.2
        score.update_score(sleep_time)


screen.exitonclick()
