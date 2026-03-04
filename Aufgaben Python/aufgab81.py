def is_prime(a):
    k=0
    for e in range(1,100000):
        if a%e == 0:
            k=k+1
    if k == 2:
        return True
    else:
        return False

for i in range(1, 100000): 

    if is_prime(i): 

        print(i, end=" ") 
