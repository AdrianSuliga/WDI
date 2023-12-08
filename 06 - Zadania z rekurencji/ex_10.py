from random import randrange
# Rekurencyjne obliczanie wyznacznika macierzy
# ================================================
# Przydatny link: https://sdjee2015.wixsite.com/whyandhow/single-post/2017/01/22/determinant-of-a-matrix-using-recursion
def determinant(T, dim):
    if dim == 1:
        return T[0][0]
    res = 0
    for i in range(dim):
        res += T[0][i] * determinant(rewriteArr(T, 0, i), dim - 1) * (-1)**i
    return res

def rewriteArr(T, row, col):
    n = len(T)
    SubT = [[0 for _ in range(n - 1)] for _ in range(n - 1)]
    rowInd, colInd = 0, 0
    
    for i in range(1, n):
        for j in range(n):
            if i != row and j != col:
                SubT[rowInd][colInd] = T[i][j]
                colInd += 1
        colInd = 0
        rowInd += 1
    return SubT

n = int(input())
T = [[randrange(1,10) for _ in range(n)] for _ in range(n)]
print(determinant(T, n))
for i in range(n):
    print(T[i])