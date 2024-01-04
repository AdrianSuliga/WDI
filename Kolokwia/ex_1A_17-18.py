"""
Dana jest tablica t[N][N] (reprezentuj¡ca szachownic¦) wypeªniona liczbami naturalnymi. Na szachownicy
znajduj¡ si¦ dwie wie»e. Prosz¦ napisa¢ funkcj¦, która odpowiada na pytanie: czy istnieje ruch wie»¡
zwi¦kszaj¡cy sum¦ liczb na "szachowanych" przez wie»e polach? Do funkcji nale»y przekaza¢ tablic¦ oraz
poªo»enia dwóch wie», funkcja powinna zwróci¢ warto±¢ logiczn¡.
Uwaga: zakªadamy, »e wie»a szachuje caªy wiersz i kolumn¦ z wyª¡czeniem pola, na którym stoi.
"""
from random import randrange
def moveTower(T:list, fstTower:tuple, sndTower:tuple):
    n = len(T)
    maxCnt = count(T, fstTower, sndTower)
    for i in range(n): # próbujemy przesunąć 1. wieżę o i pól w dół
        if -1 < fstTower[0] + i < n and not doTheyCollide((fstTower[0] + i, fstTower[1]), sndTower) and count(T, (fstTower[0] + i, fstTower[1]), sndTower) > maxCnt:
            return True # próbujmey teraz przesunąć o i pól w górę
        elif -1 < fstTower[0] - i < n and not doTheyCollide((fstTower[0] - i, fstTower[1]), sndTower) and count(T, (fstTower[0] - i, fstTower[1]), sndTower) > maxCnt:
            return True # przesunięcie o i pól w prawo
        elif -1 < fstTower[1] + i < n and not doTheyCollide((fstTower[0], fstTower[1] + i), sndTower) and count(T, (fstTower[0], fstTower[1] + i), sndTower) > maxCnt:
            return True # przesunięcie w lewo
        elif -1 < fstTower[1] - i < n and not doTheyCollide((fstTower[0], fstTower[1] - i), sndTower) and count(T, (fstTower[0], fstTower[1] - i), sndTower) > maxCnt:
            return True # teraz analogicznie dla 2. wieży
        elif -1 < sndTower[0] + i < n and not doTheyCollide(fstTower, (sndTower[0] + i, sndTower[1])) and count(T, fstTower, (sndTower[0] + i, sndTower[1])) > maxCnt:
            return True
        elif -1 < sndTower[0] - i < n and not doTheyCollide(fstTower, (sndTower[0] - i, sndTower[1])) and count(T, fstTower, (sndTower[0] - i, sndTower[1])) > maxCnt:
            return True # przesunięcie o i pól w prawo
        elif -1 < sndTower[1] + i < n and not doTheyCollide(fstTower, (sndTower[0], sndTower[1] + i)) and count(T, fstTower, (sndTower[0], sndTower[1] + i)) > maxCnt:
            return True # przesunięcie w lewo
        elif -1 < sndTower[1] - i < n and not doTheyCollide(fstTower, (sndTower[0], sndTower[1] - i)) and count(T, fstTower, (sndTower[0], sndTower[1] - i)) > maxCnt:
            return True

def doTheyCollide(t1, t2):
    if t1[0] == t2[0] and t1[1] == t2[1]: return True
    return False

def count(T, fstTower, sndTower): # funkcja liczy sumę wartości na szachowanych polach przy danym ustawieniu wież
    n = len(T)
    sum = 0
    for i in range(n): # dodajemy wszystkie w rzędach i kolumnach które szachuje wieża i odejmujemy wartości
        sum += T[fstTower[0]][i] + T[i][fstTower[1]] - 2 * T[fstTower[0]][fstTower[1]] # z pól gdzie wieża stoi
        sum += T[sndTower[0]][i] + T[i][sndTower[1]] - 2 * T[sndTower[0]][sndTower[1]] # bo policzyliśmy je podwójnie
    return sum

n = int(input())
T = [[randrange(1, 10) for _ in range(n)] for _ in range(n)]
print(moveTower(T, (0,0), (2,3)))
for i in range(n):
    print(T[i])