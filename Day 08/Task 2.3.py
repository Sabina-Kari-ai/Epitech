import turtle

pen = turtle.Turtle()

def draw_polygon(sides):
    angle = 360 / sides

    for i in range(sides):
        pen.forward(100)
        pen.right(angle)

draw_polygon(5)

turtle.done()