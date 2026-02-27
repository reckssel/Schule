wort1 = input("Bitte gebe ein Wort ein")
wort2 = input("Bitte geben sie ein Wort ein")
if (len(wort1) > len(wort2)):
    print("Das wort", wort1, "ist länger")

elif (len(wort1) < len(wort2)):
    print("Das wort", wort2, "ist länger")
else:
    print("die worte sind gleixh lang", wort2, wort1)