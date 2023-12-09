"""
Problem skoczka szachowego. Proszę napisać funkcję, która wypełnia pola szachownicy o
wymiarach NxN ruchem skoczka szachowego
"""
#brute force
def jumper(T, row, col, cnt, jumps):
    T[row][col] = cnt
    n = len(T)
    if cnt == n*n:
        printT(T)
        return True
    else:
        for jump in jumps:
            if -1 < row + jump[0] < n and -1 < col + jump[1] < n and T[row+jump[0]][col+jump[1]] == 0:
                if jumper(T, row + jump[0], col + jump[1], cnt + 1, jumps):
                    return True
        T[row][col] = 0
        return False

def printT(T):
    n = len(T)
    for i in range(n):
        for j in range(n):
            print(T[i][j],end="      ")
        print()
    print()

def ex4(n):
    T = [[0 for _ in range(n)] for _ in range(n)]
    jumps = [(-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, 1), (-2, -1)]
    jumper(T, 0, 0, 1, jumps)

n = int(input())
ex4(n)
