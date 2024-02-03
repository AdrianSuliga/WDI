"""
Dany jest ciąg zer i jedynek zapisany w tablicy T[N]. Proszę napisać funkcję, która odpowiada
na pytanie czy jest możliwe pocięcie ciągu na kawałki z których każdy reprezentuje liczbę pierwszą. Długość
każdego z kawałków nie może przekraczać 30. Na przykład dla ciągu 111011 jest to możliwe, a dla ciągu
110100 nie jest możliwe
"""
from random import randrange
def cutSeq(T, left, right):
    if check(T, left, right):
        return True
    if left == right: return False
    return cutSeq(T, left + 1, right) or cutSeq(T, left, right - 1)

def check(T, l, r):
    X, Y, Z = 0, 0, 0
    for i in range(l + 1):
        X = 10 * X + T[i]
    for i in range(l + 1, r):
        Y = 10 * Y + T[i]
    for i in range(r, len(T)):
        Z = 10 * Z + T[i]
    if checkNum(X) and checkNum(Y) and checkNum(Z): 
        return True

def checkNum(n):
    result = 0
    b = 1
    while n != 0:
        result += (n % 2) * b
        b *= 2
        n //= 10
    if isPrime(result):
        return True
    return False

def isPrime(n):
    if n == 2: return True
    if n < 2 or n % 2 == 0: return False
    b = 3
    while b <= n**(0.5):
        if n % b == 0:
            return False
        b += 2
    return True

def ex5(n):
    T = [randrange(0,2) for _ in range(n)]
    print(T)
    return cutSeq(T, 0, n-1)

n = int(input())
print(ex5(n))
