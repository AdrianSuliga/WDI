# Tablica t[N] jest wypełniona liczbami naturalnymi. Skok z pola i-tego można wykonać na pola o indeksach i+k, 
# gdzie k jest czynnikiem pierwszym liczby t[i] (mniejszym od niej samej). Napisz funkcję, która sprawdza, czy 
# da się przejść z pola 0 do N-1 – jeśli się da, zwraca ilość skoków, jeśli się nie da, zwraca -1
from random import randrange
def ex25(n):
    T = [randrange(1,1000) for _ in range(n)]
    def rec(T, ind, cnt):
        n = len(T)
        if ind == n - 1: return cnt
        if ind >= n: return -1
        res = -1
        for i in range(n):
            if isPrime(i) and T[ind] % i == 0:
                res = max(rec(T, ind + i, cnt + 1), res)
        return res
    print(T)
    return rec(T, 0, 0)

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
print(ex25(n))