"""
Kwadrat jest opisywany czwórką liczb całkowitych (x1, x2, y1, y2), gdzie x1, x2, y1, y2 oznaczają 
proste ograniczające kwadrat x1 < x2, y1 < y2. Dana jest tablica T zawierająca opisy N kwadratów. Proszę
napisać funkcję, która zwraca wartość logiczną True, jeśli danej tablicy można znaleźć 13 nienachodzących
na siebie kwadratów, których suma pól jest równa 2012 i False w przeciwnym przypadku.
"""
from random import randrange
def ex27(n):
    T = genT(n)
    def rec(T, S, ind):
        n, m = len(T), len(S)
        if m == 13 and areaSum(S) == 2022 and areApart(S):
            return True
        if m > 13 or ind == n - 1: return False
        return rec(T, S + (T[ind + 1],), ind + 1) or rec(T, S, ind + 1)
    print(T)
    return rec(T, (), -1)

def areApart(S):
    n = len(S)
    for i in range(n):
        for j in range(i + 1, n):
            if S[j][0] < S[i][0] < S[j][1] or S[j][0] < S[i][1] < S[j][i]:
                return False
            if S[j][2] < S[i][2] < S[j][3] or S[j][2] < S[i][3] < S[j][3]:
                return False
    return True

def areaSum(S):
    res = 0
    for t in S:
        res += (t[1] - t[0])**2
    return res

def genT(n):
    T = [() for _ in range(n)]
    for i in range(n):
        x1 = randrange(0, 1000)
        x2 = randrange(x1 + 1, 1000)
        y1 = randrange(0, 1000)
        y2 = y1 + x2 - x1
        T[i] = (x1,x2,y1,y2)
    return T

n = int(input("n="))
print(ex27(n))