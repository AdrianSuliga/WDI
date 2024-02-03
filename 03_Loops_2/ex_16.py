from math import sqrt
def digitSum(n):
    sum = 0
    while n != 0:
        sum += n % 10
        n //= 10
    return sum

def isItPrime(n):
    if n == 2: return True
    if n == 0 or n == 1 or n % 2 == 0: return False
    b = 3
    while b <= sqrt(n):
        if n % b == 0:
            return False
        b += 2
    return True

def factSum(n):
    b = 2
    sum = 0
    oldN = n
    while b <= sqrt(n):
        while n % b == 0:
            sum += digitSum(b)
            n //= b
        else: b += 1
    if n > 1 and n != oldN: sum += digitSum(n)
    return sum

for i in range(1, 1001):
    if digitSum(i) == factSum(i):
        print(i)