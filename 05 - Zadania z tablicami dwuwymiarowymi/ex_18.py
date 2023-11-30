from random import randrange
def lookForBiggest(T):
    n = len(T)
    biggestSum = float('-inf')
    horMoves = [(0,i) for i in range(10)]
    verMoves = [(i,0) for i in range(10)]
    for i in range(n):
        for j in range(n):
            for move in horMoves:
                sum = 0
                if -1 < j + move[1] < n:
                    for k in range(j, j+move[1]+1):
                        sum += T[i][k]
                biggestSum = max(biggestSum, sum)
            for move in verMoves:
                sum = 0
                if -1 < i + move[0] < n:
                    for k in range(i, i+move[0]+1):
                        sum += T[k][j]
                biggestSum = max(biggestSum, sum)
    return biggestSum
                
n = int(input())
T =[[randrange(-40, 41) for _ in range(n)] for _ in range(n)]
print(lookForBiggest(T))
for i in range(n):
    print(T[i])