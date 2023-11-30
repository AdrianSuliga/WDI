from random import randrange
def randTab(T, n):
    n = len(T)
    for i in range(n):
        for j in range(n):
            T[i][j] = randrange(100, 1000)

def checkNum(num):
    while num != 0:
        if (num % 10) % 2 == 0:
            return False
        num //= 10
    return True

def checkTab(T, n):
    goodRows = 0
    for i in range(n):
        for j in range(n):
            if checkNum(T[i][j]):
                goodRows += 1
                break
    if goodRows == n: return True
    else: return False

def printTab(T, n):
    n = len(T)
    for i in range(n):
        for j in range(n):
            print(T[i][j], end=' ')
        print()

n = int(input())
T = [[0 for i in range(n)] for j in range(n)]
randTab(T, n)
"""T = [[136, 179, 965],
     [701, 103, 199],
     [992, 100, 333]]"""
print(checkTab(T, n))
printTab(T, n)