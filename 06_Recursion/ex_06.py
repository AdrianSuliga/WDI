"""
Dana jest tablica T[N]. Proszę napisać funkcję, która znajdzie niepusty, najmniejszy (w sensie
liczebności) podzbiór elementów tablicy, dla którego suma elementów jest równa sumie indeksów tych elementów. 
Do funkcji należy przekazać tablicę, funkcja powinna zwrócić sumę elementów znalezionego podzbioru.
Na przykład dla tablicy: [ 1,7,3,5,11,2 ] rozwiązaniem jest liczba 10
"""
from random import randrange
def cutT(T, index, indSum, valSum):
    if indSum != 0 and indSum == valSum:
        return valSum
    if index == len(T) - 1: return -1
    return max(cutT(T, index + 1, indSum + index + 1, valSum + T[index+1]), cutT(T, index + 1, indSum, valSum))

def ex6(n):
    T = [1, 7, 3, 5, 11, 2]
    n = len(T)
    #T = [randrange(1,21) for _ in range(n)]
    return cutT(T, -1, 0, 0)

#n = int(input())
print(ex6(6))