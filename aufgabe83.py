def schaltjahr(a):
    kann = None
    if a%400 == 0:
        kann =True
    elif a%4 == 0:
        kann = True
        if a%100 == 0: kann = False
    return kann
a = int(input("Bitte gebe ein "))
if schaltjahr(a):
    print("Ist ein Schaltjahr")
else:
    print("Ist kein Schaltjahr")