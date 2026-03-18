name = str(input("Bitte Namen eingeben"))

assci = []

for buchstabe in name:
    assci.append(ord(buchstabe))
for wert in assci:
    print(wert)