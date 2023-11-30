from random import randrange
def lookForBiggest(T):
    n = len(T)
    biggestSum = 0
    result = 0, 0
    moves = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
    for i in range(n):
        for j in range(n):
            sum = 0
            for move in moves:
                if -1 < i + move[0] < n and -1 < j + move[1] < n:
                    sum += T[i+move[0]][j+move[1]]
            if sum > biggestSum:
                biggestSum = sum
                result = i,j
    return result

n = int(input())
T = [[randrange(10,100) for _ in range(n)] for _ in range(n)]
print(lookForBiggest(T))
for i in range(n):
    print(T[i])