from turtle import Turtle, Screen
import random

turtle_1 = Turtle()
turtle_2 = Turtle()
turtle_3 = Turtle()
turtle_4 = Turtle()
turtle_5 = Turtle()
turtle_6 = Turtle()

race_turtles = [turtle_1, turtle_2, turtle_3, turtle_4, turtle_5, turtle_6]
screen = Screen()


def set_turtles_position(turtles_list):
    colors = ["red", "green", "blue", "orange", "teal", "black"]
    for index in range(0, len(turtles_list)):
        turtle = turtles_list[index]
        turtle.color(colors[index])
        turtle.shape("turtle")
        turtle.penup()
        turtle.goto(-300, index * 50)
        turtle.pendown()
    return turtles_list


def start_race(turtles_list):
    positions = [10, 20, 15, 5, 6, 7, 8, 9, 0]
    colors = ["red", "green", "blue", "orange", "teal", "black"]
    finish_position = 300
    return_value = False
    for index in range(0, len(turtles_list)):
        turtle = turtles_list[index]
        if turtle.xcor() == 300:
            print(f"turtle at position {index}, {colors[index]} turtle won")
            screen.clear()
            return_value = False
        else:
            turtle.forward(random.choice(positions))
            return_value = True
    return return_value


set_turtles_position(race_turtles)
race_not_over = True
while race_not_over:
    if start_race(race_turtles) == True:
        race_not_over = True
    elif not start_race(race_turtles):
        race_not_over = False

screen.exitonclick()
screen.listen()



