import turtle
import random

t = turtle.Turtle()
t.speed(0)
t.width(2)

turtle.bgcolor("black")

for i in range(36):
    t.color(random.random(), random.random(), random.random())
    for _ in range(5):
        t.forward(150)
        t.right(144)   # sudut khusus bintang
    t.right(10)        # putar sedikit biar efek keren

t.hideturtle()
turtle.done()
