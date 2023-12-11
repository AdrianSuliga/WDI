# Tablica T[8][8] zawiera liczby naturalne. Proszę napisać funkcję, która sprawdza czy można
# wybrać z tablicy niepusty podzbiór o zadanej sumie. Warunkiem dodatkowym jest aby żadne dwa wybrane
# elementy nie leżały w tej samej kolumnie ani wierszu. Do funkcji należy przekazać wyłącznie tablicę oraz
# wartość sumy, funkcja powinna zwrócić wartość typu bool.
from random import randrange
def checkRec(T, subset, row, col, target):
    n = len(T)
    if subsetSum(subset) == target: return True
    if (row == n - 1 and col == n - 1): return False
    






def rewriteArr(row, col):
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

#n = int(input("n="))
n = 8
target = int(input("target="))
T = [[randrange(1,10) for _ in range(n)] for _ in range(n)]
#print(checkRec(T, (), -1, -1, target))
for i in range(n):
    print(T[i])
S = rewriteArr(0,0)
for i in range(n-1):
    print(S[i])