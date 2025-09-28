import turtle

def start():
    turtle.hideturtle()
    turtle.clear()
    turtle.speed(0)
    turtle.pensize(3)

    oldalhossz = 100
    eltolas_x = 40
    eltolas_y = 40

    magassag_fele = 120.7

    fuggoleges_korrekcio = 200

    start_x = -(oldalhossz / 2) - (eltolas_x / 2)
    start_y = -magassag_fele - (eltolas_y / 2) + fuggoleges_korrekcio

    elolapi_csucsok = []
    hatlapi_csucsok = []

    turtle.pencolor("blue")
    turtle.penup()
    turtle.goto(start_x, start_y)
    turtle.pendown()

    for _ in range(8):
        elolapi_csucsok.append(turtle.pos())
        turtle.forward(oldalhossz)
        turtle.right(45)

    turtle.penup()
    turtle.goto(start_x + eltolas_x, start_y + eltolas_y)
    turtle.pendown()

    for _ in range(8):
        hatlapi_csucsok.append(turtle.pos())
        turtle.forward(oldalhossz)
        turtle.right(45)

    turtle.pencolor("navy")
    for i in range(8):
        turtle.penup()
        turtle.goto(elolapi_csucsok[i])
        turtle.pendown()
        turtle.goto(hatlapi_csucsok[i])

ablak = turtle.Screen()
ablak.bgcolor("gray")

turtle.listen()
turtle.onkey(start, "h")
turtle.onkey(turtle.bye, "q")
turtle.mainloop()