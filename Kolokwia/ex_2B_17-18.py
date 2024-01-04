"""
Dana jest tablica t[N] zawieraj¡ca liczby naturalne. Prosz¦ napisa¢ funkcj¦, która odpowiada na pytanie,
czy z elementów tablicy (niekoniecznie wszystkich) mo»na utworzy¢ dwa równoliczne, niepuste podzbiory
o jednakowej sumie elementów. Do funkcji nale»y przekaza¢ wyª¡cznie tablic¦ t, funkcja powinna zwróci¢
warto±¢ typu bool.
"""
from random import randrange
def divide(T):
    def rec(T, X, Y, ind, sizeX, sizeY):
        if sizeX == sizeY and X == Y and X != 0: return (X, sizeX)
        if ind == len(T) - 1: return False
        return (rec(T, X + T[ind + 1], Y, ind + 1, sizeX + 1, sizeY) or rec(T, X, Y + T[ind + 1], ind + 1, sizeX, sizeY + 1) or
                rec(T, X, Y, ind + 1, sizeX, sizeY))
    return rec(T, 0, 0, -1, 0, 0)

n = int(input())
T = [randrange(1, 10) for _ in range(n)]
print(T)
print(divide(T))