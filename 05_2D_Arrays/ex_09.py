from random import randrange
def checkSquare(T, k):
    a, n = 2, len(T)
    while a < n:
        for i in range(n):
            for j in range(n):
                if -1 < a+i < n and -1 < a+j < n and T[i][j]*T[i+a][j]*T[i][j+a]*T[i+a][j+a] == k:
                    x, y = (2*i+a)//2, (2*j+a)//2
                    return True, (x,y)
        a += 2
    return False

k = int(input())
n = int(input())
#T = [[randrange(0,10) for _ in range(n)] for _ in range(n)]
T = [[3, 2, 7, 8, 8, 4], [3, 3, 9, 6, 7, 1], [2, 1, 3, 0, 9, 6], [4, 9, 1, 7, 1, 7], [3, 7, 7, 7, 4, 2], [4, 2, 5, 5, 3, 5]]
print(checkSquare(T,k))

for i in range(n):
    for j in range(n):
        print(T[i][j],end=' ')
    print()