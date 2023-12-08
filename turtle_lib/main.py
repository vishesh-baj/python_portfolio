import turtle
from turtle import Turtle, Screen
from random import choice
timmy_the_turtle = Turtle()

timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("teal")


def draw_square():
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)
    turtle.dot()
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)


def draw_dashed_line():
    for i in range(0, 15):
        timmy_the_turtle.forward(10)
        timmy_the_turtle.penup()
        timmy_the_turtle.forward(10)
        timmy_the_turtle.pendown()


colors = ["red", "blue", "black", "teal", "pink", "gray", "black"]


# draw shapes
def draw_shapes():
    for i in range(3, 11):
        angle = 360 / i
        for j in range(0, i):
            timmy_the_turtle.forward(100)
            timmy_the_turtle.right(angle)
        timmy_the_turtle.color(choice(colors))


draw_shapes()
screen = Screen()
screen.exitonclick()
