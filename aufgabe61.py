wort = input("Bitte ein Wort eingeben?")
buchstaben_liste  = list(wort)
i=0
for i in range(len(buchstaben_liste)):
    x = ord(buchstaben_liste[i])
    i=i+1
    print(x)


wort1 = input("Bitte ein Wort eingeben: ")

for buchstabe in wort1:
    print(ord(buchstabe))

print(*(ord(b) for b in input("Bitte ein Wort eingeben: ")), sep="\n")
