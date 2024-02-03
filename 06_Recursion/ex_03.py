"""
Szachownica jest reprezentowana przez tablicę T[8][8] wypełnioną liczbami naturalnymi zawierającymi koszt 
przebywania na danym polu szachownicy. Król szachowy znajduje się w wierszu 0 i kolumnie
k. Król musi w dokładnie 7 ruchach dotrzeć do wiersza 7. Proszę napisać funkcję, która wyznaczy minimalny
koszt przejścia króla. Do funkcji należy przekazać tablicę t oraz startową kolumnę k. Koszt przebywania na
polu startowym i ostatnim także wliczamy do kosztu przejścia
"""
from random import randrange
def king(T, row, col, minSum):
    if row == 7: return minSum

    m1, m2, m3 = float('inf'), float('inf'), float('inf')

    if -1 < row + 1 < 8 and -1 < col < 8:
        m1 = king(T, row + 1, col, minSum + T[row + 1][col])
    if -1 < row + 1 < 8 and -1 < col + 1 < 8:
        m2 = king(T, row + 1, col + 1, minSum + T[row + 1][col + 1])
    if -1 < row + 1 < 8 and -1 < col - 1 < 8:
        m3 = king(T, row + 1, col - 1, minSum + T[row + 1][col - 1])

    return min(m1,m2,m3)

def ex3(T, k):
    return king(T, 0, k, T[0][k])

k = int(input("k="))
T = [[randrange(1, 10) for _ in range(8)] for _ in range(8)]
print(ex3(T, k))
for i in range(8):
    print(T[i])