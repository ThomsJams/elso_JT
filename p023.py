import turtle

def start():
    import random
    turtle.hideturtle()
    turtle.clear()
    turtle.penup()
    turtle.goto(-75, 37.5)
    turtle.pendown()
    turtle.pencolor("red")
    turtle.pensize(5)

    for _ in range(3):
        turtle.forward(150)
        turtle.right(120)

ablak = turtle.Screen()
ablak.bgcolor("gray")

turtle.listen()
turtle.onkey(start, "h")
turtle.onkey(turtle.bye, "q")
turtle.mainloop()