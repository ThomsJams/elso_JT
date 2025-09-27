#2. alkalom
import random
'''szam = int(input("Kérek egy számot: "))
if szam > 0:
    print("Pozitív")
elif szam < 0:
    print("Negatív")
else:
    print("Nulla")'''

'''szam = input("Kérek egy számot: ")
if szam.isdigit():
    szam = int(szam)
    if szam > 0:
        print("Pozitív")
    elif szam < 0:
        print("Negatív")
    else:
        print("Nulla")
else:
    print("Nem számot adtál meg!")

jegy = int(input("Kérek egy érdemjegyet: "))
while jegy == 1 or jegy > 5 or jegy < 1:
    jegy = int(input("Kérek egy érdemjegyet: "))
    if jegy == 10:
        print("Hibátlan!")
        break
else:
    print("Jól teljesített!")
print("Gratulálunk")

kocka = random.randint(1, 6)
while True:
    tipp = int(input("Kérek egy számot: "))
    if tipp == kocka:
        break
print("Sikerült kitalálni!")

uzenet = "Jó reggelt"
for betu in uzenet:
    print (betu)
    if betu == " ":
        break

lista = (1, 4, 7)
for elem in lista:
    print(elem)

for elem in range(5):
    print("Nem leszek többet rossz")

for _ in range(1,4):
    print("Nem leszek többet rossz")

def fv():
    pass

for elem in range(1,6):
    if elem == 1:
        continue
    print(elem, "Nem leszek többet rossz")

try:
    print(10/0)
except ZeroDivisionError:
    print("Hiba! Nullával osztás!")
except NameError:
    print("Névhiba")
    
print("OK")'''

while True:
    try:
        szam = int(input("Kérek egy számot: "))
    except:
        print("Nem egész számot adtál meg")
    else:
        break