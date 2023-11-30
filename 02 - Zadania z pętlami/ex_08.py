import math

def isItPrime(n):
    if n == 2: return True
    if n == 1 or n % 2 == 0: return False  
    b = 3
    while b <= math.sqrt(n):
        if n % b == 0:
            return False
        else:
            b += 1
    return True

for i in range(1, 101, 1):
    print(isItPrime(i), i)