import time
import turtle
from random import randrange

# Screeeen
screen = turtle.Screen()
screen.title('Behold of mighty Ssssnake')
screen.setup(600, 600)
screen.tracer(0)

side = turtle.Turtle()

side.pensize(10)
side.right(90)
side.forward(400)
side.left(120)
side.forward(350)
side.left(60)
side.forward(400)
side.left(120)
side.forward(350)
side.left(60)
side.forward(400)
side.right(120)
side.forward(350)
side.right(60)
side.forward(400)
side.right(120)
side.forward(350)
side.left(60)
side.forward(350)
side.left(120)
side.forward(350)
side.left(60)
side.forward(350)
side.left(120)
side.forward(350)

sssnake = []
for i in range(3):
    sssnake_segment = turtle.Turtle()
    sssnake_segment.shape('square')
    sssnake_segment.penup()
    if i > 0:
        sssnake_segment.color('red')
    sssnake.append(sssnake_segment)

food = turtle.Turtle()
food.shape('circle')
food.color('red')
food.penup()
food.goto(randrange(-300, 300, 20), randrange(-300, 300, 20))


screen.onkeypress(lambda: sssnake[0].setheading(90), 'w')
screen.onkeypress(lambda: sssnake[0].setheading(270), 's')
screen.listen()

while True:
    if sssnake[0].distance(food) < 10:
        food.goto(randrange(-300, 300, 20), randrange(-300, 300, 20))
        sssnake_segment = turtle.Turtle()
        sssnake_segment.shape('square')
        sssnake_segment.penup()
        if i > 0:
            sssnake_segment.color('gray')
        sssnake.append(sssnake_segment)

    x_cor = sssnake[0].xcor()
    y_cor = sssnake[0].ycor()
    if 0 < x_cor < 303.11 and -400 < y_cor < 0:
        sssnake[0].setheading(30)
        screen.onkeypress(lambda: sssnake[0].setheading(30), 'd')
        screen.onkeypress(lambda: sssnake[0].setheading(210), 'a')

    if -303.11 < x_cor < 0 and -400 < y_cor < 0:
        sssnake[0].setheading(330)
        screen.onkeypress(lambda: sssnake[0].setheading(330), 'd')
        screen.onkeypress(lambda: sssnake[0].setheading(150), 'a')

    for i in range(len(sssnake) - 1, 0, -1):
        x = sssnake[i - 1].xcor()
        y = sssnake[i - 1].ycor()
        sssnake[i].goto(x, y)

    # snake head movement
    sssnake[0].forward(20)

    screen.update()
    time.sleep(0.1)
