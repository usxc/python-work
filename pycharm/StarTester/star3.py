from turtle import *


def draw_star(length=200):
    shape("turtle")
    for i in range(5):
        forward(length)
        left(144)


colormode(255)
penup()
forward(300)
pendown()

draw_star()  # length200が使われる
draw_star(100)

done()
