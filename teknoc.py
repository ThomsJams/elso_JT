import turtle

def negyszog(x, y):
    kerulet = 2 * x + 2 * y
    terulet = y * x
    if x == y:
        alakzat = "negyzet"
    else:
        alakzat = "teglalap"
    return kerulet, terulet, alakzat

def negyzet():
    turtle.penup()
    turtle.goto(-50, 50)
    turtle.pendown()
    turtle.pencolor("black")
    turtle.pensize(5)

    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)

def pont(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.dot(5, "Black")

def dobas():
    import random
    turtle.hideturtle()
    turtle.clear()
    negyzet()
    szam = random.randint(1, 6)

    if szam == 1:
        pont(0, 0)
    elif szam == 2:
        pont(-30, 30)
        pont(30, -30)
    elif szam == 3:
        pont(0, 0)
        pont(-30, 30)
        pont(30, -30)
    elif szam == 4:
        pont(30, 30)
        pont(-30, -30)
        pont(-30, 30)
        pont(30, -30)
    elif szam == 5:
        pont(0, 0)
        pont(30, 30)
        pont(-30, -30)
        pont(-30, 30)
        pont(30, -30)
    elif szam == 5:
        pont(30, 0)
        pont(30, 30)
        pont(-30, -30)
        pont(-30, 30)
        pont(30, -30)
        pont(-30, 0)


ablak = turtle.Screen()

turtle.listen()
turtle.onkey(dobas, "d")
turtle.onkey(turtle.bye, "Escape")
turtle.mainloop()