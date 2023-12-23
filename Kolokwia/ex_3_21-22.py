"""
Na szachownicy o wymiarach N x N wypełnionej liczbami naturalnymi > 1 odbywają się wyścigi
wież. Pierwsza wieża startuje z lewego górnego rogu i ma dotrzeć do prawego dolnego rogu szachownicy. 
Pierwsza wieża może wykonywać tylko ruchy w prawo lub w dół szachownicy. Druga wieża
startuje z prawego górnego rogu i ma dotrzeć do lewego dolnego rogu szachownicy. Druga wieża
może wykonywać tylko ruchy w lewo lub w dół szachownicy. Wygrywa wieża, która dotrze do mety
w mniejszej liczbie ruchów. Wieże mogą wykonać ruch z jednego pola na drugie tylko wtedy, gdy
liczby na obu polach są względnie pierwsze.
Proszę napisać funkcję, która dla danej tablicy zwraca numer wieży, która wygra wyścig lub 0, jeżeli
wyścig będzie nierozstrzygnięty. Można założyć, że podczas wyścigu wieże nie spotkają się na jednym
polu. Po wykonaniu funkcji zawartość tablicy nie może ulec zmianie.
"""
from random import randrange
def racistTowers(T): # funkcja sprawdza w ile ruchów wieże 1. i 2. dotrą do swoich celów
    n = len(T)
    r1, r2 = rook1(T, n, 0, 0, 0), rook2(T, n, 0, n - 1, 0)
    if r1 < r2: return 1
    elif r1 > r2: return 2
    else: return 0

def rook1(T, n, row, col, cnt): # funkcja licząca w ilu ruchach wieża 1 startująca z (0, 0) dotrze do (n - 1, n - 1)
    if row == n - 1 and col == n - 1: return cnt
    if row >= n or col >= n: return float('inf')
    res = float('inf')
    for i in range(1, n): # idziemy w dół
        if row + i < n and checkNumbers(T[row][col], T[row + i][col]):
            res = min(rook1(T, n, row + i, col, cnt + 1), res)
    for i in range(1, n): # idziemy w prawo
        if col + i < n and checkNumbers(T[row][col], T[row][col + i]):
            res = min(rook1(T, n, row, col + i, cnt + 1), res)
    return res

def rook2(T, n, row, col, cnt):
    if row == n - 1 and col == 0: return cnt
    if row >= n or col < 0: return float('inf')
    res = float('inf')
    for i in range(1, n): # idziemy w dół
        if row + i < n and checkNumbers(T[row][col], T[row + i][col]):
            res = min(rook2(T, n, row + i, col, cnt + 1), res)
    for i in range(1, n): # idziemy w lewo
        if col - i > -1 and checkNumbers(T[row][col], T[row][col - i]):
            res = min(rook2(T, n, row, col - i, cnt + 1), res)
    return res

def checkNumbers(n1, n2): #sprawdzam czy 2 liczby są względnie pierwsze czyli czy nwd(n1, n2) == 1?
    while n2 != 0:
        n1, n2 = n2, n1 % n2
    if n1 == 1: return True
    else: return False

n = 4
T = [[randrange(2, 100) for _ in range(n)] for _ in range(n)]
print(racistTowers(T))
for i in range(n):
    print(T[i])
