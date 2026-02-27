wort=str(input("Bitte geben sie ein wort ein")).lower().replace(' ', '')
uw=wort[::-1]
if wort == uw:
    print("Es ist ein Palendrom")
else:
    print("Es ist kein Palendrom")