import turtle

size = 20
turtle.penup()
turtle.sety(270)
turtle.setx(-320)
turtle.pendown()
turtle.width(2)
turtle.shape("arrow")
turtle.speed(10)
turtle.bgcolor("#76EE00")
turtle.pensize(2)
turtle.pencolor("Black")


def hilbert(level, angle):
    if level == 0:
        return False
    size = 10

    turtle.right(angle)
    hilbert(level - 1, -angle)

    turtle.forward(size)
    turtle.left(angle)
    hilbert(level - 1, angle)
    turtle.forward(size)
    hilbert(level - 1, angle)
    turtle.left(angle)
    turtle.forward(size)
    hilbert(level - 1, -angle)
    turtle.right(angle)


hilbert(4, 90)
