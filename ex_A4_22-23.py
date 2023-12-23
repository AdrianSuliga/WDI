"""
Na szachownicy o rozmiarach N × N reprezentowanej przez tablicę T[N][N] umieszczono pewną liczbę
skoczków. Położenie skoczka w tablicy oznaczono liczbą 1, puste pola oznaczono liczbą 0. Część pustych pól
na szachownicy jest szachowana przez znajdujące się na niej skoczki. Proszę zaproponować funkcję place(T),
która znajdzie na szachownicy puste pole położone najbliżej środka szachownicy, takie że umieszczenie tam
skoczka maksymalnie zwiększy liczbę szachowanych pustych pól. Do funkcji przekazujemy tablicę T zawierającą położenie skoczków. 
Funkcja powinna zwrócić pole (wiersz, kolumna), na którym należy umieścić
skoczka. Odległość pomiędzy polami: (w1, k1) i (w2, k2) jest równa max(abs(w1 − w2), abs(k1 − k2))
"""
def jumpers(T):
    n = len(T)
    maxMoves, maxDist = countChecks(n, T), float('inf')
    result = (0,0)
    for i in range(n):
        for j in range(n):
            if T[i][j] == 0:
                T[i][j] = 1
                checks = countChecks(n, T)
                if checks >= maxMoves:
                    maxMoves = checks
                    pt = (i,j)
                    if dist(pt, n) < maxDist:
                        maxDist = dist(pt, n)
                        result = pt
                T[i][j] = 0
    return result

def dist(point, n):
    middle = (n/2, n/2)
    return max(abs(point[0] - middle[0]), abs(point[1] - middle[1]))

def countChecks(n, T):
    moves = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]
    for i in range(n):
        for j in range(n):
            if T[i][j] == 1 or T[i][j] == 3:
                for move in moves:
                    if -1 < i + move[0] < n and -1 < j + move[1] < n and T[i+move[0]][j+move[1]] == 0:
                        T[i + move[0]][j + move[1]] = 2
                    elif -1 < i + move[0] < n and -1 < j + move[1] < n and T[i + move[0]][j + move[1]] == 1:
                        T[i + move[0]][j + move[1]] = 3
    cnt = 0
    for i in range(n):
        for j in range(n):
            if T[i][j] == 2 or T[i][j] == 3:
                T[i][j] -= 2
                cnt += 1
    return cnt

T = [[0, 1, 0, 0],
     [1, 1, 0, 0],
     [0, 0, 1, 0],
     [1, 0, 0, 0]]
#print(jumpers(T))
print(countChecks(4, T))
