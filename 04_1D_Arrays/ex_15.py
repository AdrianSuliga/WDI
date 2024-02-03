from math import sqrt
from random import randrange
def checkT(t):
    n = len(t)
    for i in range(n):
        if isFib(i) and isPrime(t[i]):
            return False
    for i in range(n):
        if not isFib(i) and isPrime(t[i]):
            return True
    return False

def isPrime(n):
    if n == 2: return True
    if n < 2 or n % 2 == 0: return False
    b = 3
    while b <= sqrt(n):
        if n % b == 0:
            return False
        b += 1
    return True

def isFib(n):
    fibL, fibM, fibR = 1, 1, 1
    while fibR <= n:
        if fibR == n: return True
        fibL = fibM
        fibM = fibR
        fibR = fibL + fibM
    return False

n = int(input())
t = [randrange(10, 100) for _ in range(n)]
print(checkT(t))
print(t)