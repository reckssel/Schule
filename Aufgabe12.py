print("aufgabe 1.2")
x=int(input("Bitte gebe Stunden ein"))
y=int(input("Bitte gebe minuten ein"))
z=int(input("Bitte gebe das wie lange das projekt brauch ein"))

e=z+y
if e > 59:
    x=x+e/60
    y=e%60
else:
    y=e

print("End: ", x, ":", y)