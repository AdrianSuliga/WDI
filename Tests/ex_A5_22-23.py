"""
Dana jest tablica T[N][N] wypełniona liczbami naturalnymi, na której możemy wykonywać operacje:
• rotacji elementów danego wiersza w prawo,
• rotacji elementów danej kolumny w dół.
Tablicę taką nazywamy kwadratem magicznym, wtedy gdy suma elementów w każdym wierszu i każdej kolumnie jest jednakowa. 
Proszę napisać funkcję magic(T), która sprawdza czy po wykonaniu dokładnie dwóch
dowolnych operacji tablica T stanie się kwadratem magicznym. Funkcja powinna zwrócić T rue albo F alse.
"""
def magic(T):
    n = len(T)
    for i in range(n):
        for j in range(n):
            for m in range(n):
                for k in range(n):
                    rotateRow(T, i)
                    rotateRow(T, m)
                    if isMagicSquare(T): return True
                    rotateBackRow(T, m)
                    rotateBackRow(T, i)
                    rotateRow(T, i)
                    rotateCol(T, k)
                    if isMagicSquare(T): return True
                    rotateBackCol(T, k)
                    rotateBackRow(T, i)
                    rotateCol(T, j)
                    rotateRow(T, m)
                    if isMagicSquare(T): return True
                    rotateBackRow(T, m)
                    rotateBackCol(T, j)
                    rotateCol(T, j)
                    rotateCol(T, k)
                    if isMagicSquare(T): return True
                    rotateBackCol(T, j)
                    rotateBackCol(T, k)
    return False
                    
def rotateBackRow(T, rowToRotate):
    n = len(T)
    rem = T[rowToRotate][0]
    for i in range(n - 1):
        T[rowToRotate][i] = T[rowToRotate][i + 1]
    T[rowToRotate][n - 1] = rem

def rotateBackCol(T, colToRotate):
    n = len(T)
    rem = T[0][colToRotate]
    for i in range(n - 1):
        T[i][colToRotate] = T[i + 1][colToRotate]
    T[n - 1][colToRotate] = rem

def rotateRow(T, rowToRotate):
    n = len(T)
    rem = T[rowToRotate][n - 1]
    for i in range(n - 1, 0, -1):
        T[rowToRotate][i] = T[rowToRotate][i - 1]
    T[rowToRotate][0] = rem

def rotateCol(T, colToRotate):
    n = len(T)
    rem = T[n - 1][colToRotate]
    for i in range(n - 1, 0, -1):
        T[i][colToRotate] = T[i - 1][colToRotate]
    T[0][colToRotate] = rem

def isMagicSquare(T):
    n = len(T)
    sum = sumRow(T, 0)
    for i in range(n):
        if sumRow(T, i) != sum:
            return False
        if sumCol(T, i) != sum:
            return False
    return True
    
def sumRow(T, row):
    sum = 0
    for i in range(len(T)):
        sum += T[row][i]
    return sum

def sumCol(T, col):
    sum = 0
    for i in range(len(T)):
        sum += T[i][col]
    return sum

T = [[3, 11, 14, 17], 
     [6, 12, 7, 9],
     [10, 8, 16, 13],
     [5, 15, 4, 2]]
print(magic(T))