from random import randrange
def randTab(T,n):
    for i in range(n):
        for j in range(n):
            T[i][j] = randrange(0, 10)

def calcDiv(T,n):
    minRow, maxCol = 1000, 0
    r, c = 0, 0
    rowSums = [0 for _ in range(n)]
    colSums = [0 for _ in range(n)]
    for i in range(n):
        for j in range(n):
            colSums[j] += T[i][j]
            rowSums[i] += T[i][j]
    for i in range(n):
        if rowSums[i] < minRow:
            minRow = rowSums[i]
            r = i
    for i in range(n):
        if colSums[i] > maxCol:
            maxCol = colSums[i]
            c = i
    return r,c

def printTab(T,n):
    for i in range(n):
        for j in range(n):
            print(T[i][j],end=' ')
        print()
    

n = int(input())
T = [[0 for i in range(n)] for j in range(n)]
randTab(T, n)
print(calcDiv(T,n))
printTab(T,n)