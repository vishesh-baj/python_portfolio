from turtle import  Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)


def backward():
    tim.backward(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(turn_left, key="a")
screen.onkey(turn_right, key="d")
screen.onkey(backward, key="s")
screen.onkey(clear, key="c")


screen.exitonclick()
