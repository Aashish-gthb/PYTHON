from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

SHAPE = ((-5, 0), (-3, 0), (-3, 5), (3, 5), (3, 0), (5, 0), (5, -4), (3, -4),
         (3, -5), (2, -5), (2, -4), (-2, -4), (-2, -5), (-3, -5), (-3, -4), (-5, -4))


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.set_car_shape()
    def new_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car =Turtle(shape="square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250,250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)


    def move_car(self):
        self.hideturtle()
        for car in self.all_cars:
            car.backward(self.car_speed)
            for car in self.all_cars:
                if car.xcor() < -320:
                    self.all_cars.remove(car)


    def level_up(self):
        self.car_speed += MOVE_INCREMENT            

    def set_car_shape(self):
        self.getscreen().register_shape(name="car", shape=SHAPE)
        self.shape("car")
        self.shapesize(stretch_wid=4, stretch_len=2)


