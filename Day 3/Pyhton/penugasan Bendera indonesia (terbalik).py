import turtle

t = turtle.Turtle()
t.speed(3)

# Function to draw rectangle
def draw_rectangle(color, width, height):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

# Start position
t.penup()
t.goto(-150, 100)
t.pendown()

# Red part (top)
draw_rectangle("white", 300, 100)

# Move down for white part
t.right(90)
t.forward(100)
t.left(90)

# White part (bottom)
draw_rectangle("red", 300, 100)

t.hideturtle()
turtle.done()