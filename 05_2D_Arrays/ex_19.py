from random import randrange
def countPairs(T, target):
    moves = [(-1, 2), (1,2), (2,1), (2,-1)]
    cnt, n = 0, len(T)
    for i in range(n):
        for j in range(n):
            for move in moves:
                if -1 < i + move[0] < n and -1 < j + move[1] < n and T[i][j] * T[i + move[0]][j + move[1]] == target:
                    cnt += 1
    return cnt

x = int(input())
T = [[randrange(1,10) for _ in range(x)] for _ in range(x)]
"""
T = [[3, 1, 2, 1],
     [1, 2, 2, 1],
     [1, 3, 2, 3],
     [2, 2, 1, 3]]
"""
print(countPairs(T, x))
for i in range(x):
    for j in range(x):
        print(T[i][j],end=' ')
    print()