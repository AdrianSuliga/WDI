import math
import time
# sito: False - złożone, True - pierwsze
def sieve(size):
    a = [True] * size
    a[0] = False
    a[1] = False
    for i in range(size):
        if a[i]:
            for j in range(i*i, size, i):
                a[j] = False
    return a

# zmiana sita na listę liczb pierwszych
def sieveToArray(size):
    sArray = sieve(size)
    numbers = []
    b = 0
    for p in sArray:
        if p:
            numbers.append(b)
        b+=1
    return numbers

# dfs - zwraca False jeśli nie ma liczby pierwszej o danej sumie cyfr
# lub zwraca liczbę pierwszą o szukanej sumie
def dfs(position, remainder, base=0, primes = None):
    if primes == None:
        upperLimit = math.ceil(10**(position/2))
        primes = sieveToArray(upperLimit)

    if 9*position < remainder:
        return False
    if remainder < 0:
        return False
    if position == 0:
        for p in primes:
            if base % p == 0:
                return False
        return base
    for d in range(10):
        recursiveCall = dfs(position=position-1, remainder=remainder-d, base=base + d*10**(position - 1), primes=primes)
        if recursiveCall: return recursiveCall
    return False

#i - ilość cyfr
def smallestPrime(sum):
    i = 1
    while True:
        r = dfs(i, sum)
        if r: return r
        i+=1

start = time.time()
print(smallestPrime(101))
end = time.time()
print(end - start)