"""
Na szachownicy o wymiarach N × N umieszczono pewną liczbę pionków. Położenie pionków opisuje lista [(w0, k0),(w1, k1),(w2, k2), ...]. 
W lewym górnym rogu szachownicy (o współrzędnych 0, 0) znajduje się
król, który musi dotrzeć do prawego dolnego rogu szachownicy. Król może wykonywać ruchy w prawo, w
dół lub w górę szachownicy, nie może zbijać pionków ani wracać na pole, na którym już był. Proszę napisać
funkcję king(N,L), która zwróci maksymalną liczbę ruchów jakie może wykonać król na drodze do celu. Do
funkcji należy przekazać wyłącznie dwa parametry: rozmiar szachownicy N oraz listę L zawierającą położenia pionków. 
Jeżeli dotarcie do celu nie jest możliwe funkcja powinna zwrócić wartość None.
"""
from random import randrange
def kingsPath(n, L, row, col, cnt, banned):
    if row == n - 1 and col == n - 1: return cnt
    if row >= n or row < 0 or col >= n: return None
    for pawn in L:
        if row == pawn[0] and col == pawn[1]: return None
    k1, k2, k3 = None, None, None
    if -1 < row + 1 < n and row + 1 != banned[0]:
        k1 = kingsPath(n, L, row + 1, col, cnt + 1, (row,col))
    if -1 < row - 1 < n and row - 1 != banned[0]:
        k2 = kingsPath(n, L, row - 1, col, cnt + 1, (row,col))
    if -1 < col + 1 < n and col + 1 != banned[1]:
        k3 = kingsPath(n, L, row, col + 1, cnt + 1, (row,col))
    maxi = 0
    if k1 != None: maxi = max(maxi, k1)
    if k2 != None: maxi = max(maxi, k2)
    if k3 != None: maxi = max(maxi, k3)
    if maxi == 0: return None
    else: return maxi

def ex3Main(n:int, L:list):
    return kingsPath(n, L, 0, 0, 0, (-1,-1))

n = 5
L = []
print(ex3Main(n, L))