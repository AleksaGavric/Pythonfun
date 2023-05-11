# Seizure warning... (I'm not kidding)

import turtle
import time
import random


def setup_turtle():
    """Set up the turtle graphics window with initial configuration."""
    turtle.turtlesize(0.03)
    turtle.speed(10)


def blue_screen():
    """Change the background color to black."""
    turtle.bgcolor("black")


def key_press():
    """Change the background color to white."""
    turtle.bgcolor("white")


def draw_forward():
    """Draw a spiral using the turtle graphics."""
    for x in range(101):
        turtle.forward(x)
        turtle.right(random.randint(1, 30))
        time.sleep(0.07)
        blue_screen()
        time.sleep(0.07)
        key_press()


if __name__ == "__main__":
    setup_turtle()
    turtle.listen()
    turtle.onkeypress(blue_screen, "space")
    turtle.onkeypress(key_press, "a")
    draw_forward()
    turtle.done()
