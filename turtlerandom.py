import turtle, time, random

turtle.turtlesize(0.03)
turtle.speed(10)

def blue_screen():
    turtle.bgcolor("Black")
def keyy():
    turtle.bgcolor("White")

"""turtle.listen()
turtle.onkeypress(blue_screen, 'space')
turtle.onkeypress(keyy, "a")"""

def ff():
        for x in range(101):
            turtle.forward(x)
            turtle.right(random.randint(1,30))
            time.sleep(0.07)
            blue_screen()
            time.sleep(0.07)
            keyy()
ff()


    


