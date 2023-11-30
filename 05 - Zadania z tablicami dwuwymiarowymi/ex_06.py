def findMaxInT(T, n):
    result = 0
    for i in range(n):
        if T[i][n-1] > result:
            result = T[i][n-1]
    return result

def singletones(T1, T2, n):
    maxT = findMaxInT(T1, n)
    T3 = [0 for _ in range(maxT + 1)]
    for i in range(n):
        for j in range(n):
            T3[T1[i][j]] += 1
    it = 0
    for i in range(1, maxT + 1):
        if T3[i] == 1:
            T2[it] = i
            it += 1

n = 6
T1 = [[1, 3, 6, 9, 10, 11],
      [3, 5, 7, 11, 14, 19],
      [1, 2, 5, 9, 19, 22],
      [3, 45, 66, 77, 88, 100],
      [9, 10, 23, 34, 43, 45],
      [10, 11, 12, 13, 14, 15]]
T2 = [0 for _ in range(n*n)]
singletones(T1, T2, n)
print(T2)

