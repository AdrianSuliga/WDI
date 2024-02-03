"""
Dana jest tablica T[N][N] wypełniona wartościami 0, 1. Każdy wiersz tablicy traktujemy jako liczbę zapisaną
w systemie dwójkowym o długości N bitów. Stała N jest rzędu 1000. Proszę zaimplementować funkcję
distance(T), która dla takiej tablicy wyznaczy dwa wiersze, dla których różnica zawartych w wierszach
liczb jest największa. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić odległość pomiędzy
znalezionymi wierszami. Można założyć, że żadne dwa wiersze nie zawierają identycznego ciągu cyfr.
"""
from random import randrange
def searchArray(T): # funkcja porównuje każdy wierszy z każdym o numerze większym od niego
    n = len(T) # 
    maxDist, cDist = -float('inf'), 0
    res = (-1, -1)
    for i in range(n):
        for j in range(i + 1, n): # zaczynamy od i + 1, bo wiersze wsześniej już zdążyliśmy porównać w poprzednich iteracjach
            if i == j: continue # takich samy wierszy nie ma co sprawdzać
            cDist = calcDist(T, i, j)
            if cDist > maxDist:
                res = (i,j)
                maxDist = cDist
    return res

def calcDist(T, i, j):
    dist = 0
    n = len(T)
    for k in range(n):
        if T[i][k] == T[j][k]: continue # jeśli dwie komórki są takie same to nie wpływają na odległość wierszy
        if T[i][k] == 1: 
            dist += T[i][k] * 2**(n - k) # jeśli w i. wierszu jest 1 to dodajemy do odl
            continue
        if T[j][k] == 1: 
            dist -= T[j][k] * 2**(n - k) # jeśli w j. wierszu jest 1 to odejmujemy od odl
            continue
    return abs(dist) # zwracamy bez znaku aby bez problemów porównywać

n = int(input())
T = [[randrange(0,2) for _ in range(n)] for _ in range(n)]
print(searchArray(T))
for i in range(n):
    print(T[i])