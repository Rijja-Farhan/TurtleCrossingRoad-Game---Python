from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

#car manager constructor
class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.Create_cars() #calling the create_cars function


#creating cars
    def Create_cars(self):
        random_num = random.randint(-250,300)#starting form -250 so that there are no cars on the turtle at starting position
        self.shape("square")
        self.shapesize(1,5)
        self.setheading(180)
        self.penup()
        self.goto(340,random_num)
        self.color(random.choice(COLORS))#giving colors to the cars from colors list





#function to move the cars towards left
    def move(self,all_cars):

        for cars in all_cars:
            new_x = cars.xcor() - 10
            cars.goto(new_x,cars.ycor())
    def detect(self,all_cars,turtle):
        for cars in all_cars:
            if cars.xcor() > 0:
             if  turtle.distance(cars) < 20 :   # Adjust the value as needed
                    print("Game Over")
                    return True
