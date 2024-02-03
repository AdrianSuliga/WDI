def findMaxT(T, n):
    maxT = 0
    for i in range(n):
        for j in range(n):
            if T[i][j] > maxT:
                maxT = T[i][j]
    return maxT

def writeToT(T1, T2, n):
    maxT = findMaxT(T1, n)
    T3 = [0 for _ in range(maxT + 1)]
    for i in range(n):
        for j in range(n):
            T3[T1[i][j]] += 1
    it = 0
    for i in range(maxT + 1):
        while T3[i] > 0:
            T2[it] = i
            it += 1
            T3[i] -= 1
n = 6
T1 = [[1, 3, 6, 9, 11, 11],
      [3, 7, 7, 11, 11, 19],
      [1, 2, 5, 9, 9, 22],
      [3, 45, 77, 77, 100, 100],
      [9, 10, 23, 34, 45, 45],
      [10, 11, 13, 13, 15, 15]]
T2 = [0 for _ in range(n**2)]
writeToT(T1, T2, n)
print(T2)