import turtle

turtle.speed(0)
turtle.bgcolor("black")

for i in range(15):
    for color in ('red', 'blue', 'green', 'white', 'magenta', 'yellow', 'cyan'):
        turtle.color(color)
        turtle.pensize(3)
        turtle.left(4)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)