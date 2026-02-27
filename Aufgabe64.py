betrag = float(input("ReChchnungsbetrag"))
g = float(input("Gezahlter Betragg"))

rü = round(g - betrag, 2)
print("===========================")
print("Rückgeld: ", rü, "EUR")
print("===========================")
rü = rü * 100

e2 = e1 = c50 = c20 = c10 = c5 = c2 = c1 = 0

while rü > 0:
    if rü >= 200:
        e2 += 1
        rü -= 200
    elif rü >= 100:
        e1 += 1
        rü -= 100
    elif rü >= 50:
        c50 += 1
        rü -= 50
    elif rü >= 20:
        c20 += 1
        rü -= 20
    elif rü >= 10:
        c10 += 1
        rü -= 10
    elif rü >= 5:
        c5 += 1
        rü -= 5
    elif rü >= 2:
        c2 += 1
        rü -= 2
    else:
        c1 += 1
        rü -= 1

print("Cent 1", c1)
print("Cent 2", c2)
print("Cent 5", c5)
print("Cent 10", c10)
print("Cent 20", c20)
print("Cent 50", c50)
print("1 Euro", e1)
print("2 Euro", e2)