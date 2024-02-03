# Zadanie jak powyżej. Funkcja sprawdzająca czy król może dostać się z pola w,k do któregokolwiek z narożników
from random import randrange
def king(w, k, T):
    return URKing(w, k, T) or BRKing(w, k, T) or BLKing(w, k, T)

def URKing(w, k, T):
    n = len(T)
    if w == 0 and k == n - 1: return True
    if w >= n or k >= n: return False

    k1, k2, k3 = False, False, False
    if -1 < w - 1 < n and -1 < k + 1 < n and canMove(T[w][k], T[w - 1][k + 1]):
        k1 = URKing(w - 1, k + 1, T)
    if -1 < w - 1 < n and -1 < k < n and canMove(T[w][k], T[w - 1][k]):
        k2 = URKing(w - 1, k, T)
    if -1 < w < n and -1 < k + 1 < n and canMove(T[w][k], T[w][k + 1]):
        k3 = URKing(w, k + 1, T)
    return k1 or k2 or k3

def BRKing(w, k, T):
    n = len(T)
    if w == n - 1 and k == n - 1: return True
    if w >= n or k >= n: return False

    k1, k2, k3 = False, False, False
    if -1 < w + 1 < n and -1 < k + 1 < n and canMove(T[w][k], T[w + 1][k + 1]):
        k1 = BRKing(w + 1, k + 1, T)
    if -1 < w + 1 < n and -1 < k < n and canMove(T[w][k], T[w + 1][k]):
        k2 = BRKing(w + 1, k, T)
    if -1 < w < n and -1 < k + 1 < n and canMove(T[w][k], T[w][k + 1]):
        k3 = BRKing(w, k + 1, T)
    return k1 or k2 or k3

def BLKing(w, k, T):
    n = len(T)
    if w == n - 1 and k == 0: return True
    if w >= n or k >= n: return False

    k1, k2, k3 = False, False, False
    if -1 < w + 1 < n and -1 < k - 1 < n and canMove(T[w][k], T[w + 1][k - 1]):
        k1 = BLKing(w + 1, k - 1, T)
    if -1 < w + 1 < n and -1 < k < n and canMove(T[w][k], T[w+1][k]):
        k2 = BLKing(w + 1, k, T)
    if -1 < w < n and -1 < k - 1 < n and canMove(T[w][k], T[w][k - 1]):
        k3 = BLKing(w, k - 1, T)
    return k1 or k2 or k3

def canMove(n1, n2):
    x1, x2 = n1 % 10, 0
    while n2 != 0:
        x2 = n2 % 10
        n2 //= 10
    if x1 < x2: return True
    return False

n = int(input("n = "))
row = int(input("row baginning: "))
col = int(input("col beginning: "))
T = [[randrange(10, 100) for _ in range(n)] for _ in range(n)]
print(king(row, col, T))
for i in range(n):
    print(T[i])