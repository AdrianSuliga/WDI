"""
Dana jest tablica wypeªniona liczbami naturalnymi int t[N][N] reprezentuj¡ca szachownicę. Proszę napisać
funkcję, która sprawdza, czy jest mo»liwe ustawienie dwóch wzajemnie szachujących się skoczków tak, aby
suma warto±ci pól, na których stoją skoczki, była liczbą pierwszą. Do funkcji należy przekazać tablicę t,
funkcja powinna zwrócić wartość typu bool.
"""
from random import randrange
def placeJumpers(t):
    n = len(t)
    moves = [(2, 1), (2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(n):
        for j in range(n):
            for move in moves:
                if -1 < i + move[0] < n and -1 < j + move[1] < n and isPrime(t[i][j] + t[i + move[0]][j + move[1]]):
                    return True
    return False

def isPrime(n):
    if n == 2: return True
    if n < 2 or n % 2 == 0: return False
    b = 3
    while b <= n**(0.5):
        if n % b == 0:
            return False
        b += 2
    return True

n = int(input())
t = [[randrange(1, 10) for _ in range(n)] for _ in range(n)]
print(placeJumpers(t))
for i in range(n):
    print(t[i])
