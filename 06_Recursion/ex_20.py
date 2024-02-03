# Zadanie jak powyżej. Funkcja powinna dostarczyć drogę króla w postaci tablicy zawierającej
# kierunki (liczby od 0 do 7) poszczególnych ruchów króla do wybranego celu
from random import randrange
def king(rS, cS, rE, cE, T, res):
    n = len(T)
    if rS == rE and cS == cE: 
        print(res)
        return True
    if rS >= n or cS >= n: 
        return False

    if rE != 0 and cE != 0:
        moves = [(1,1), (1,0), (0,1)]
    elif rE == 0:
        moves = [(-1,1), (-1,0), (0,1)]
    elif cE == 0:
        moves = [(1,-1), (1,0), (0,-1)]

    for move in moves:
        if -1 < rS + move[0] < n and -1 < cS + move[1] < n and canMove(T[rS][cS], T[rS + move[0]][cS + move[1]]):
            if king(rS + move[0], cS + move[1], rE, cE, T, res + (T[rS + move[0]][cS + move[1]],)):
                return True
    return False

def canMove(n1, n2):
    x1 = n1 % 10
    x2 = 0
    while n2 != 0:
        x2 = n2 % 10
        n2 //= 10
    if x1 < x2: return True
    return False

def ex20(n):
    T = [[randrange(10,100) for _ in range(n)] for _ in range(n)]
    rs = int(input("starting row: "))
    cs = int(input("starting column: "))
    if not king(rs, cs, n - 1, n - 1, T, (T[rs][cs],)): print("()")
    if not king(rs, cs, n - 1, 0, T, (T[rs][cs],)): print("()")
    if not king(rs, cs, 0, n - 1, T, (T[rs][cs],)): print("()")
    for i in range(n):
        print(T[i])

n = int(input())
ex20(n)
