from random import randrange
def checkT(T, n):
    for i in range(n):
        flag = True
        for j in range(n):
            if not checkNum(T[i][j]):
                flag = False
                break
        if flag: return True, i
    return False
        
def checkNum(num):
    while num != 0:
        if num % 2 == 0:
            return True
        num //= 10
    return False

n = int(input())
T = [[randrange(100,1000) for _ in range(n)] for _ in range(n)]
print(checkT(T, n))
for i in range(n):
    for j in range(n):
        print(T[i][j],end=' ')
    print()