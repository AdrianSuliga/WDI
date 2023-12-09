# Problem 8 hetmanów
# ========================
# Rozwiązanie heurystyczne - rozstawiamy hetmany o ruch skoczka szachowego

def placeQueens(T, n, moves):
    def rec(T, n, row, col, cnt, moves):
        T[row][col] = cnt
        if cnt == n:
            printT(T)
            return True
        for move in moves:
            while -1 < row + move[0] < n and -1 < col + move[1] < n and canPlace(row + move[0], col + move[1], T):
                rec(T, n, row + move[0], col + move[1], cnt, moves)
    for i in range(n):
        rec(T, n, 0, i, 1, moves)
        printT(T)
        T[0][i] = 0
        print()

def canPlace(row, col, T):
    n = len(T)
    for i in range(n):
        if T[row][i] != 0: return False
        if T[i][col] != 0: return False
        if -1 < row + i < n and -1 < col + i < n and T[row + i][col + i] != 0: return False
        if -1 < row - i < n and  -1 < col - i < n and T[row - i][col - i] != 0: return False
        if -1 < row + i < n and -1 < col - i < n and T[row + i][col - i] != 0: return False
        if -1 < row - i < n and -1 < col + i < n and T[row - i][col + i] != 0: return False
    return True

def printT(T):
    for i in range(len(T)):
        print(T[i])

def ex15(n):
    T = [[0 for _ in range(n)] for _ in range(n)]
    moves = [(1, 2), (-1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, 1), (-2, -1)]
    placeQueens(T, n, moves)

n = int(input())
ex15(n)