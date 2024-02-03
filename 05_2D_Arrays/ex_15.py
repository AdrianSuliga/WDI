from random import randrange
def checkT(T):
    n = len(T)
    for i in range(n):
        flag = True
        for j in range(n):
            if not containsPrimeDigit(T[i][j]):
                flag = False
                break
        if flag: return True
    return False

def containsPrimeDigit(n):
    while n != 0:
        if n % 10 == 2 or n % 10 == 3 or n % 10 == 5 or n % 10 == 7:
            return True
        n //= 10
    return False

n = int(input())
T = [[randrange(100,1000) for _ in range(n)] for _ in range(n)]
print(checkT(T))
for i in range(n):
    print(T[i])