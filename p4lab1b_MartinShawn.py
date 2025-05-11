import turtle

# Set up turtle
t = turtle.Turtle()
t.pensize(5)
t.color("darkgreen")

# Draw the letter S
t.penup()
t.goto(-100, 0)  # Starting position for 'S'
t.pendown()
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)

# Move to position for 'M'
t.penup()
t.goto(15, 0)  # Starting position for 'M'
t.setheading(90)  # Point turtle upwards
t.pendown()

# Draw the letter M
t.forward(100)
t.right(135)
t.forward(70)
t.left(90)
t.forward(70)
t.right(135)
t.forward(100)

# Finish
t.hideturtle()
turtle.done()
