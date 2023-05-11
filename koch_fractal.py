import turtle


def setup_turtle():
    """Set up the turtle graphics window with initial configuration."""
    turtle.penup()
    turtle.setx(-500)
    turtle.sety(-190)
    turtle.pendown()
    turtle.width(1)
    turtle.speed(10)
    turtle.bgcolor("#76EE00")
    turtle.pensize(0.001)
    turtle.shape("classic")


def koch(level, size):
    """
    Recursive function to draw the Koch snowflake fractal.

    Args:
        level (int): The current level of recursion.
        size (float): The size of the line segment to be drawn.
    """
    if level == 0:
        turtle.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            print("GO")
            koch(level - 1, size / 3)
            print("LOOP")
            turtle.left(angle)
            print(angle)


def draw_crazy_koch():
    """Draws a crazy Koch snowflake fractal using the turtle graphics."""
    for x in range(1, 2):
        turtle.penup()
        turtle.setx(-250)
        turtle.pendown()
        turtle.clear()
        koch(10, 500000)


setup_turtle()
draw_crazy_koch()
turtle.done()
