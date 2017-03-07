n = 1

while n < 101:
    if n % 5 == 0 and n % 3 ==0:
        print("CracklePop")
    elif n % 3 == 0:
        print("Crackle")
    elif n % 5 == 0:
        print("Pop")
    else:
        print(n)

    n += 1
