def pseudoSort(T2, T1, n):
    for i in range(n):
        for j in range(n):
            if isItSingletone(T1[i][j], T1):
                push(T1[i][j], T2)

def isItSingletone(num, T1):
    flag = False
    n = len(T1)
    for i in range(n):
        for j in range(n):
            if T1[i][j] == num and not flag:
                flag = True
            elif T1[i][j] == num and flag:
                return False
    return True

def push(num, T2):
    n = len(T2)
    index = 0
    while T2[index] < num:
        if T2[index] == 0: break
        index += 1
    while index < n:
        T2[index], num = num, T2[index]
        index += 1

n = 6
T1 = [[1, 3, 6, 9, 10, 11],
      [3, 5, 7, 11, 14, 19],
      [1, 2, 5, 9, 19, 22],
      [3, 45, 66, 77, 88, 100],
      [9, 10, 23, 34, 43, 45],
      [10, 11, 12, 13, 14, 15]]
T2 = [0 for _ in range(n**2)]
pseudoSort(T2, T1, n)
print(T2)