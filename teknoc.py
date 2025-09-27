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

ablak = turtle.Screen()

turtle.listen()
turtle.onkey(turtle.bye, "Escape")
turtle.mainloop()


if __name__ == "__main__":
    a = 4
    b = 3
    eredmeny = negyszog(a, b)
    print(f"A {eredmeny[2]} kerulet ", eredmeny[0])
    print(f"A {eredmeny[2]} terület ", eredmeny[1])