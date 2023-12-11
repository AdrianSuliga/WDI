# Dana jest tablica T[N] zawierająca liczby naturalne. Po tablicy możemy przemieszczać się
# według następującej zasady: z pola o indeksie i możemy przeskoczyć na pole o indeksie i+k jeżeli k jest
# czynnikiem pierwszym liczby t[i] mniejszym od t[i]. Proszę napisać funkcję, która zwraca informację czy jest
# możliwe przejście z pola o indeksie 0 na pole o indeksie N-1. Funkcja powinna zwrócić liczbę wykonanych
# skoków lub wartość -1 jeżeli powyższe przejście nie jest możliwe
from random import randrange
def ex22(n):
    T = [randrange(1,100) for _ in range(n)]
    def rec(T, ind, moves):
        n = len(T)
        if ind == n - 1: 
            return moves
        if ind >= n: return -1
        cnt = -1
        for i in range(n):
            if isPrime(i) and T[ind] % i == 0:
                cnt = max(rec(T, ind + i, moves + 1), cnt)
        return cnt
    print(rec(T, 0, 0))
    print(T)

def isPrime(n):
    if n == 2: return True
    if n < 2 or n % 2 == 0: return False
    b = 3
    while b <= n**(0.5):
        if n % b == 0:
            return False
        b += 2
    return True

n = int(input("n="))
ex22(n)