# Tablica T[8][8] zawiera liczby naturalne. Proszę napisać funkcję, która sprawdza czy można
# wybrać z tablicy niepusty podzbiór o zadanej sumie. Warunkiem dodatkowym jest aby żadne dwa wybrane
# elementy nie leżały w tej samej kolumnie ani wierszu. Do funkcji należy przekazać wyłącznie tablicę oraz
# wartość sumy, funkcja powinna zwrócić wartość typu bool.
from random import randrange
def ex21(n, target):
    def checkRec(T, subset, target):
        n = len(T)
        if subsetSum(subset) == target: 
            print(subset)
            return True
        if T == []: return False
        for i in range(n):
            for j in range(n):
                if checkRec(rewriteArr(T, i, j), subset + (T[i][j],), target):
                    return True
        return False
    T = [[randrange(1,10) for _ in range(n)] for _ in range(n)]
    print(checkRec(T, (), target))
    for i in range(n):
        print(T[i])

def rewriteArr(T, row, col):
    n = len(T)
    S = [[0 for _ in range(n - 1)] for _ in range(n - 1)]
    rIt = 0
    cIt = 0
    for i in range(n):
        for j in range(n):
            if i != row and j != col:
                S[rIt][cIt] = T[i][j]
                if cIt == n - 2:
                    cIt = 0
                    rIt += 1
                else: cIt += 1
    return S

def subsetSum(set):
    res = 0
    for s in set:
        res += s
    return res

n = int(input("n="))
target = int(input("target="))
ex21(n, target)