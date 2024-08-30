from turtle import Turtle,Screen
import random


screen = Screen()
is_race_on = False
screen.setup(width=500,height=400)
user_bet =screen.textinput(title="Make your bet!",prompt="Which turtle will win the race? Enter a colour: ")
colors = ["red", "orange", "yellow", "green", "blue", "violet","indigo"]
y_positions = [-150,-100,-50,0,50,100,150]

all_turtles = []

for turtle_index in range(7):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.teleport(x=-230,y=y_positions[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True


while is_race_on:
    
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on =False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You've won! the {winning_colour} turtle is the winner")
            else:    
                print(f"You've lost! the {winning_colour} turtle is the winner")
        random_distance = random.randint(1,10)
        turtle.forward(random_distance)


screen.exitonclick()