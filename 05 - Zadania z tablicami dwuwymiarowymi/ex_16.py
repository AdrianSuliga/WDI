from random import randrange
def checkT(T):
    n = len(T)
    for i in range(n):
        flag = False
        for j in range(n):
            if containsAllPrimeDigits(T[i][j]):
                flag = True
                break
        if not flag: return False, i
    return True

def containsAllPrimeDigits(num):
    while num != 0:
        if num % 10 != 2 and num % 10 != 3 and num % 10 != 5 and num % 10 != 7:
            return False
        num //= 10
    return True

n = int(input())
T = [[randrange(100, 1000) for _ in range(n)] for _ in range(n)]
print(checkT(T))
for i in range(n):
    print(T[i])