"""
. Na zbiorze liczb całkowitych określono trzy operacje: A,B,C przekształcające liczby:
 A: zwiększa liczbę o 3;
 B: podwaja liczbę;
 C: wszystkie nieparzyste cyfry w liczbie zmniejsza o 1, np. 2356->2246, 2020->2020.
Proszę napisać funkcję która sprawdza czy można przekształcić liczbę X na liczbę Y w nie więcej niż N krokach.
Do funkcji należy przekazać wartości X,Y,N, funkcja powinna zwrócić minimalną liczbę operacji przekształcającą liczbę
X w Y lub wartość -1 jeżeli takie przekształcenie nie istnieje. Uwaga: zabronione jest używanie kolejno dwóch tych
samych operacji.
"""
from math import log10
def transform(X, Y, N): # 46, 27, 5
    def rec(X, Y, N, bannedMove, moves):
        if moves <= N and X == Y: return moves
        elif moves == N and X != Y: return float('inf') 
        minMoves = float('inf')
        if bannedMove == 0:
            minMoves = min(rec(B(X), Y, N, 1, moves + 1), rec(C(X), Y, N, 2, moves + 1), minMoves)
        elif bannedMove == 1:
            minMoves = min(rec(A(X), Y, N, 0, moves + 1), rec(C(X), Y, N, 2, moves + 1), minMoves)
        elif bannedMove == 2:
            minMoves = min(rec(A(X), Y, N, 0, moves + 1), rec(B(X), Y, N, 1, moves + 1), minMoves)
        else:
            minMoves = min(rec(A(X), Y, N, 0, moves + 1), rec(B(X), Y, N, 1, moves + 1), rec(C(X), Y, N, 2, moves + 1))
        return minMoves
    res = rec(X, Y, N, -1, 0)
    if res == float('inf'): return -1
    else: return res

def A(X):
    return X + 3
def B(X):
    return X * 2
def C(X):
    size = int(log10(X) + 1)
    arr = [0 for _ in range(size)]
    it = size - 1
    while X != 0:
        arr[it] = X % 10
        X //= 10
        it -= 1
    for i in range(size):
        if arr[i] % 2 == 1:
            arr[i] -= 1
    it, res = size - 1, 0
    for i in range(size):
        res += arr[i] * 10**it
        it -= 1
    return res

print(transform(23,39,4))