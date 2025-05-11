import turtle

# Set up turtle
t = turtle.Turtle()
t.pensize(2)

# Draw a square using a for loop
t.color("blue")
for _ in range(4):
    t.forward(100)
    t.right(90)

# Draw a triangle using a for loop
t.color("red")
for _ in range(3):
    t.forward(100)
    t.left(120)

# Finish
turtle.done()
