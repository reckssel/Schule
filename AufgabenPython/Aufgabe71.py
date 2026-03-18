pin = [1, 2, 3, 4]
j=0
ein = str(input("gebe deinen Code ein"))

for zahl in ein:
    
    if ein == str(pin[j]):
        j+=1
    else:
        print("False")

if j==4:
    print("Seccesfull") 