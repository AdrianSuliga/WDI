import math
#Oryginalne podejście do problemu SmallestPrimeWithSum101

def isItPrime(n):
    b = 2
    while b <= math.sqrt(n):
        if (n % b == 0):    
            return False       
        else:
            b = b + 1
    return True

def getSum(n):
    sum = 0
    for x in str(n):
        sum = sum + int(x)
    return sum

b = 299999999999

while True:
    print(b)
    if getSum(b) == 101 and isItPrime(b) == True:
        print(b)
        break
    b = b+9
