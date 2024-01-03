"""
Dwie liczby naturalne są czynnikowo-podobne, jeżeli w swoich rozkładach na czynniki pierwsze mają
dokładnie jeden czynnik równy. Na przykład: 24 i 14 albo 32 i 18. Dana jest tablica T[N][N]
zawierająca liczby naturalne. Dwie liczby sąsiadują ze sobą wtedy, gdy leżą w sąsiednich kolumach i
sąsiednich wiersza. Proszę napisać funkcję three(T), która zwraca ilość liczb w tablicy sąsiadujących
dokładnie z 3 liczbami czynnikowo-podobnymi.
"""
from random import randrange
def three(T):
    n = len(T)
    moveset = [(-1,-1), (-1,1), (1,-1), (1,1)]
    mainCnt = 0
    for i in range(n):
        for j in range(n):
            tempCnt = 0
            for move in moveset:
                if -1 < i + move[0] < n and -1 < j + move[1] < n and czySaCzynnikowoPodobne(T[i][j], T[i + move[0]][j + move[1]]):
                    tempCnt += 1
            if tempCnt == 3: 
                mainCnt += 1
    return mainCnt

def czySaCzynnikowoPodobne(n1, n2):
    b, cnt = 2, 0
    while b <= min(n1, n2):
        while n1 % b == 0 and n2 % b == 0:
            cnt += 1
            n1 //= b
            n2 //= b
        b += 1
    if cnt == 1: return True
    else: return False

n = int(input())
T = [[randrange(1,10) for _ in range(n)] for _ in range(n)]
print(three(T))
for i in range(n):
    print(T[i])
