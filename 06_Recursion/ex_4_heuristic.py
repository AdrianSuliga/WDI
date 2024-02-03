"""
Problem skoczka szachowego. Proszę napisać funkcję, która wypełnia pola szachownicy o
wymiarach NxN ruchem skoczka szachowego
"""
def jumperH(T, moves, row, col, cnt):
    T[row][col] = cnt
    n = len(T)
    if cnt == n**2:
        printT(T)
        return True
    else:
        moveToDo, x, minCnt = (), 0, float('inf')
        for move in moves:
            if -1 < row + move[0] < n and -1 < col + move[1] < n and T[row + move[0]][col + move[1]] == 0:
                x = howManyPossibleMoves(T, moves, row + move[0], col + move[1])
                if x < minCnt:
                    minCnt = x
                    moveToDo = move
        jumperH(T, moves, row + moveToDo[0], col + moveToDo[1], cnt + 1)

# ile ruchów można wykonać z pola (r,c) na tablicy T mając dostępny moveset konia
def howManyPossibleMoves(T, moves, r, c):
    cnt, n = 0, len(T)
    for move in moves:
        if -1 < r + move[0] < n and -1 < c + move[1] < n and T[r + move[0]][c + move[1]] == 0:
            cnt += 1
    return cnt

def printT(T):
    n = len(T)
    for i in range(n):
        print(T[i])

def ex4(n):
    T = [[0 for _ in range(n)] for _ in range(n)]
    jumps = [(-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, 1), (-2, -1)]
    jumperH(T, jumps, 0, 0, 1)

n = int(input())
ex4(n)