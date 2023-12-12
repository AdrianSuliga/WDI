"""
Dana jest tablica T[N] zawierająca liczby naturalne. Proszę napisać funkcję, która odpowiada
na pytanie, czy spośród (niekoniecznie wszystkich) elementów tablicy można utworzyć dwa podzbiory o
jednakowej sumie elementów, tak aby suma mocy obu podzbiorów wynosiła k. Do funkcji należy przekazać
wyłącznie tablicę T oraz liczbę naturalną k, funkcja powinna zwrócić wartość typu bool.
"""
from random import randrange
def ex32(T:list, k:int):
    def rek(T:list, S1:int, S2:int, P:int, k:int, ind:int):
        if S1 == S2 and P == k: return True
        if ind == len(T) - 1: return False
        return rek(T, S1 + T[ind + 1], S2, P + 1, k, ind + 1) or rek(T, S1, S2 + T[ind + 1], P + 1, k, ind + 1) or rek(T, S1, S2, P, k, ind + 1)
    return rek(T, 0, 0, 0, k, -1)

n = int(input("n="))
k = int(input("k="))
T = [randrange(1, 100) for _ in range(n)]
print(ex32(T, k))
#print(T)