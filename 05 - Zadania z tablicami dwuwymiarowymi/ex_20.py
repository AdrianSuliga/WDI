from random import randrange
def sum_rows(T, n, row):
    sum = 0
    for i in range(n):
        sum += T[row][i]
    return sum

def sum_cols(T, n, col):
    sum = 0
    for i in range(n):
        sum += T[i][col]
    return sum

def twoTowers(n, T):
    result = [(0, 0), (0, 0)]
    biggestSum, sum = -1, 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for m in range(n):
                    if i == k and j == m: continue
                    elif i == k and j != m:
                        sum += sum_rows(T, n, i) + sum_cols(T, n, j) + sum_cols(T, n, m) - 2*T[i][j] - 2*T[k][m]
                    elif i != k and j == m:
                        sum += sum_rows(T, n, i) + sum_rows(T, n, k) + sum_cols(T, n, m) - 2*T[i][j] - 2*T[k][m]
                    else:
                        sum += sum_rows(T, n, i) + sum_rows(T, n, k) + sum_cols(T, n, j) + sum_cols(T, n, m) - 2*T[i][j] - 2*T[k][m] - T[i][m] - T[k][j]
                    if sum > biggestSum:
                        biggestSum = sum
                        result[0], result[1] = (i,j), (k, m)
                    sum = 0
    return biggestSum, result                 
n = int(input())
T = [[randrange(0,10) for _ in range(n)] for _ in range(n)]
print(twoTowers(n, T))
for i in range(n):
    for j in range(n):
        print(T[i][j],end=' ')
    print()





