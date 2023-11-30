from random import randrange
def checkT(T, ind, X, Y, Z):
    if ind == len(T) - 1:
        if X == Y == Z: return True
        else: return False
    return checkT(T, ind + 1, X + wage(T[ind+1]), Y, Z) or checkT(T, ind + 1, X, Y + wage(T[ind+1]), Z) or checkT(T, ind + 1, X, Y, Z + wage(T[ind+1]))

def wage(n):
    if n < 2: return 0
    b = 2
    cnt = 0
    while b <= n**(0.5):
        if n % b == 0: cnt += 1
        while n % b == 0:
            n //= b
        b += 1
    if n > 1: cnt += 1
    return cnt

def ex2(T):
    return checkT(T, -1, 0, 0, 0)

n = int(input("n="))
T = [randrange(100,1000) for _ in range(n)]
print(ex2(T))
