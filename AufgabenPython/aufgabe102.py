b=float(input("Rechnungsbetrag: "))
g=float(input("Gezahlter Betrag: "))
r=round((g-b) * 100)
e = {50_000:0, 20_000:0, 10_000:0, 5_000:0, 2_000:0, 1_000:0, 500:0, 200:0, 100:0, 50:0, 20:0, 10:0, 5:0, 2:0, 1:0}
for i in e:
    while r >= i:
        e[i] += 1
        r -= i
print("=================")
print("Rückgeld:", r)
print("=================")
for x, y in e.items():
    if x >= 100:
        print(f"{x/100} €: {y}")
    else:
        print(f"{x} Cent: {y}")