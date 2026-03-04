
def ausgabe():
    for row in p:
        print("\t".join(row))
def eingabe():
    print("Eingabe")
    a = int(input("Reihe: "))
    b = int(input("Platz: "))
    return a, b
def schleif():
    k = 0
    while k != 1:
        k = int(input("Beenden(1) Weiter(2): "))
        if k == 2:
            a, b = eingabe()
            if p[a][b] == "o":
                print("Der Platz ist schon reserviert")
            else:
                p[a][b] = "o"
                ausgabe()

p = [["" for _ in range(26)] for _ in range(16)]
k = 0
for x in range(16):
    for y in range(26):
        if y == 0:
            p[x][y] = str(x)
        elif x == 0:
            p[x][y] = str(y)
        else:
            p[x][y] = "x"

schleif()