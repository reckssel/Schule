import random
x = random.randint(1,100)
h = True
def überprüfen(k, x):
    y = None
    if k > x:
        print("Ist kleiner")
        y = True
    elif k < x:
        print("Ist größer")
        y = True
    else:
        print("glückwunsch richtig")
        y = False
    return y
def eingabe():
    k=int(input("Bitte Zahl eingen"))
    return k
while h:
    h = überprüfen(eingabe(), x)
print("Herzlichen Glückwusch")