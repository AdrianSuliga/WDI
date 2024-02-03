from random import randrange
def zerujNieKomplementarne(T, n):
    for i in range(n):
        for j in range(n):
            if not czyMaPare(T[i][j], T, n):
                T[i][j] = 0
    
def czyMaPare(num, T, n):
    for i in range(n):
        for j in range(n):
            if czySaKomplementarne(T[i][j], num):
                return True
    return False

def czySaKomplementarne(a, b):
    n = a + b
    if n == 2: return True
    if n < 2 or n % 2 == 0: return False
    b = 3
    while b <= n**(1/2):
        if n % b == 0:
            return False
        b += 2
    return True

n = int(input())
T = [[randrange(10,100) for _ in range(n)] for _ in range(n)]
for i in range(n):
    print(T[i])
zerujNieKomplementarne(T, n)
print()
for i in range(n):
        print(T[i])