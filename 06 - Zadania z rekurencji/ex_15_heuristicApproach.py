# Problem 8 hetmanów
# ========================
# Rozwiązanie heurystyczne - rozstawiamy hetmany o ruch skoczka szachowego

def countSolutions(T, n, row, col):
    pass

def printT(T):
    for i in range(len(T)):
        print(T[i])

def ex15(n):
    T = [[0 for _ in range(n)] for _ in range(n)]
    print(countSolutions(T, n, 0, 0))
    printT(T)

n = int(input())
ex15(n)