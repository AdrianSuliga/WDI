# Dana jest tablica T[N]. Proszę napisać program wypisujący wszystkie podzbiory o określonym iloczynie.
# X to krotka z z podzbiorem T, product() liczy iloczyn wszystkich elementów krotki
from random import randrange
def rec(T, target, ind, X):
    if product(X) == target: 
        print(X)
        return True
    if ind == len(T) - 1: return False
    rec(T, target, ind + 1, X + (T[ind + 1],))
    rec(T, target, ind + 1, X)

def product(X):
    if len(X) == 0: return 0
    res = 1
    for el in X:
        res *= el
    return res

def ex12(T, target):
    rec(T, target, -1, ())
    print(T)

n = int(input("n="))
target = int(input("target="))
T = [randrange(1,10) for _ in range(n)]
ex12(T, target)
