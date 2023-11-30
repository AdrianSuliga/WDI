def spiral(n):
    T = [[0 for i in range(n)] for j in range(n)]
    toIns = 10
    row_min, col_min = 0, 0
    row_max, col_max = n - 1, n - 1

    while row_min <= row_max:
        for i in range(col_min, col_max + 1):
            T[row_min][i] = toIns
            toIns += 1
        row_min += 1
        for i in range(row_min, row_max + 1):
            T[i][col_max] = toIns
            toIns += 1
        col_max -= 1
        for i in range(col_max, col_min - 1, -1):
            T[row_max][i] = toIns
            toIns += 1
        row_max -= 1
        for i in range(row_max, row_min - 1, -1):
            T[i][col_min] = toIns
            toIns += 1
        col_min += 1

    for i in range(n):
        for j in range(n):
            print(T[i][j], end=' ')
        print()

n = int(input())
spiral(n)