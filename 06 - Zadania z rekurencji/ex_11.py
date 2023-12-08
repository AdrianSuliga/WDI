# Dana jest tablica T[N]. Proszę napisać program zliczający liczbę podzbiorów o określonym iloczynie.
# X to krotka z z podzbiorem T, product() liczy iloczyn wszystkich elementów krotki
from random import randrange
def lookRecursively(T, target, X, ind):
    if product(X) == target: return 1
    if ind == len(T) - 1: return 0
    return lookRecursively(T, target, X + (T[ind + 1],), ind + 1) + lookRecursively(T, target, X, ind + 1)

def product(X):
    if len(X) == 0: return 0
    res = 1
    for el in X:
        res *= el
    return res

n = int(input())
target = int(input())
T = [randrange(1, 10) for _ in range(n)]
print(lookRecursively(T, target, (), -1))
print(T)