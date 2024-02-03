from random import randrange
def trojki(T):
    n, cnt = len(T), 0
    for i in range(n-2):
        if nwd(T[i],T[i+1],T[i+2]) == 1:
            cnt += 1
    for i in range(n-3):
        if nwd(T[i],T[i+1],T[i+3]) == 1:
            cnt += 1
    for i in range(n-3):
        if nwd(T[i],T[i+2],T[i+3]) == 1:
            cnt += 1
    for i in range(n-4):
        if nwd(T[i],T[i+2],T[i+4]) == 1:
            cnt += 1
    return cnt
        
def nwd(a, b, c):
    while b != 0:
        a, b = b, a%b
    while c != 0:
        a, c = c, a%c
    return a

n = int(input())
T = [randrange(10,100) for _ in range(n)]
print(trojki(T))
print(T)