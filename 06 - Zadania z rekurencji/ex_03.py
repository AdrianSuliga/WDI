from random import randrange
def king(T, row, col, minSum):
    if row == 7: return minSum

    m1, m2, m3 = float('inf'), float('inf'), float('inf')

    if -1 < row + 1 < 8 and -1 < col < 8:
        m1 = king(T, row + 1, col, minSum + T[row + 1][col])
    if -1 < row + 1 < 8 and -1 < col + 1 < 8:
        m2 = king(T, row + 1, col + 1, minSum + T[row + 1][col + 1])
    if -1 < row + 1 < 8 and -1 < col - 1 < 8:
        m3 = king(T, row + 1, col - 1, minSum + T[row + 1][col - 1])

    return min(m1,m2,m3)

def ex3(T, k):
    return king(T, 0, k, T[0][k])

k = int(input("k="))
T = [[randrange(1, 10) for _ in range(8)] for _ in range(8)]
print(ex3(T, k))
for i in range(8):
    print(T[i])