zahl1 = int(input("Bitte gebe eine Zahl ein: "))
zahl2 = 1
erg = 1

while zahl2 <= zahl1:
    erg = erg * zahl2
    zahl2 = zahl2 + 1

print(erg)
