'''def teglalp():
    a = 5
    b = 4
    kerulet = 2 * a + 2 * b
    return kerulet

a = 4
b = 3
print("A kerület ", teglalp())

def teglalap_ker(a, b):
    #a = 5
    #b = 4
    kerulet = 2 * a + 2 * b
    return kerulet

a = 4
b = 3
print("A kerület ", teglalap_ker(a, b))

def teglalap_ter(x, y):
    terulet = y * x
    return terulet

x = 4
y = 3
print("A terület ", teglalap_ter(x, y))

def teglalap_ker_ter(x, y):
    kerulet = 2 * x + 2 * y
    terulet = y * x
    return kerulet, terulet

x = 4
y = 3
print("A kerulet ", teglalap_ker_ter(x, y)[0])
print("A terület ", teglalap_ker_ter(x, y)[1])'''

def negyszog(x, y):
    kerulet = 2 * x + 2 * y
    terulet = y * x
    if x == y:
        alakzat = "negyzet"
    else:
        alakzat = "teglalap"
    return kerulet, terulet, alakzat

a = 4
b = 3
eredmeny = negyszog(a, b)
print(f"A {eredmeny[2]} kerulet ", eredmeny[0])
print(f"A {eredmeny[2]} terület ", eredmeny[1])