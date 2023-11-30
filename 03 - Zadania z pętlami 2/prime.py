from math import sqrt
def isItPrime(n):
    if n == 2: return True
    if n == 0 or n == 1 or n % 2 == 0: return False
    b = 3
    while b <= sqrt(n):
        if n % b == 0:
            return False
        b += 2
    return True
def printFactorsOf(n):
    b = 1
    while b <= sqrt(n):
        if b == sqrt(n) and n % b == 0:
            print(b, end=' ')
        elif n % b == 0:
            print(b, n//b, end = ' ')
        b += 1


n = int(input("n="))
for i in range(1, n+1, 1):
    #print(isItPrime(i), i)
    print(i, end = "   ")
    printFactorsOf(i)
    print()