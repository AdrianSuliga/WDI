from random import randrange
def square(T):
    n, a = len(T), 1
    while a < n:
        for i in range(n):
            for j in range(n):
                if -1 < i+a < n and -1 < j+a < n and checkNum(T[i][j] * T[i+a][j] * T[i][j+a] * T[i+a][j+a]):
                    return a + 1
        a += 1
    return 0

def checkNum(num):
    d1, d2 = 0, 0
    if num == 1: return False
    b = 2
    while b <= num**(1/2):
        if num % b == 0:
            if (d1 == 0 and d2 == 0) or b == d1:
                d1 = b
            elif (d1 != 0 and d2 == 0) or b == d2:
                d2 = b
            elif b != d1 and b != d2 and d1 != 0 and d2 != 0:
                return False
            num //= b
        else: b += 1
    if num > 1:
        if (d1 == 0 and d2 == 0) or num == d1:
            d1 = num
        elif (d1 != 0 and d2 == 0) or num == d2:
            d2 = num
        elif num != d1 and num != d2 and d1 != 0 and d2 != 0: 
            return False
    if d1 == 0 or d2 == 0: return False
    return True

n = int(input())
T = [[randrange(1,10) for _ in range(n)] for _ in range(n)]
print(square(T))
for i in range(n):
    print(T[i])