import turtle
import random

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
    pass

def dobas():
    turtle.clear()
    negyzet()

#app
ablak = turtle.Screen()

turtle.listen()
turtle.onkey(dobas, "d")
turtle.onkey(turtle.bye, "Escape")
turtle.mainloop()


if __name__ == "__main__":
    a = 4
    b = 3
    eredmeny = negyszog(a, b)
    print(f"A {eredmeny[2]} kerulet ", eredmeny[0])
    print(f"A {eredmeny[2]} terület ", eredmeny[1])