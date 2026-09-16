import turtle

pen = turtle.Turtle()
pen.color("magenta")
pen.speed(0)

for i in range(36):
    pen.circle(80)
    pen.right(10)

turtle.done()