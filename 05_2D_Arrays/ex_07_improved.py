def rewrite(T1, T2, n):
    for i in range(n):
        for j in range(n):
            push(T1[i][j], T2)

def push(num, T2):
    index = 0
    while T2[index] < num:
        if T2[index] == 0: break
        index += 1
    while index < len(T2):
        T2[index], num = num, T2[index]
        index += 1

n = 6
T1 = [[1, 3, 6, 9, 11, 11],
      [3, 7, 7, 11, 11, 19],
      [1, 2, 5, 9, 9, 22],
      [3, 45, 77, 77, 100, 100],
      [9, 10, 23, 34, 45, 45],
      [10, 11, 13, 13, 15, 15]]
T2 = [0 for _ in range(n**2)]
rewrite(T1, T2, n)
print(T2)

