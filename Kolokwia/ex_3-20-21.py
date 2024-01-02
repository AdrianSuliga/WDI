"""
Dana jest tablica T[N][N] (reprezentująca szachownicę) wypełniona liczbami całkowitymi. 
Proszę zaimplementować funkcję chess(T) która ustawia na szachownicy dwie wieże, tak aby suma liczb na
„szachowanych” przez wieże polach była największa. Do funkcji należy przekazać tablicę, funkcja powinna
zwrócić położenie wież w postaci krotki (row1, col1, row2, col2).
Uwaga: zakładamy, że pola na których znajdują się wieże nie są szachowane.
"""
from random import randrange
def chess(T):
    n = len(T)
    maxSum, res = -float('inf'), (-1, -1, -1, -1)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for m in range(n): # sprawdzamy wszystkie możliwe ustawienia 2 wież, (i,j) to wsp. pierwszej, a (k,m) - drugiej
                    if i == k and j == m: continue # gdy stoją na tym samym polu to nie ma to sensu
                    sum = calcSum(T, i, j, k, m)
                    if sum > maxSum:
                        maxSum = sum
                        res = (i, j, k, m)
    return res

def calcSum(T, r1, c1, r2, c2):
    sum = 0
    n = len(T)
    for i in range(n):
        sum += T[i][c1]
        sum += T[r1][i]
        sum += T[i][c2]
        sum += T[r2][i]
    sum -= 2 * T[r1][c1] + 2 * T[r2][c2]
    return sum

n = int(input())
T = [[randrange(1,10) for _ in range(n)] for _ in range(n)]
print(chess(T))
for i in range(n):
    print(T[i])