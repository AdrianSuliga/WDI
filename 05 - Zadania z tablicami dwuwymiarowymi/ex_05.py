from random import randrange
def checkT(T, n):
    rowSums, colSums = [0 for _ in range(n)], [0 for _ in range(n)]
    # zlicz sumy liczb we wszystkich wierszach i kolumnach
    for i in range(n):
        rowSums[i] = sum_row(T, i)
        colSums[i] = sum_col(T, i)

    maxCol, minRow = float('-inf'), float('inf')
    x, y = 0, 0
    # znajdź maksymalną dodatnią sumę kolumn i minimalną dodatnią sumę wierszy, x i y to współrzędne punktu odpowiadającemu
    # owej maksymalnej sumie
    for i in range(n):
        if colSums[i] > maxCol and colSums[i] > 0:
            maxCol = colSums[i]
            y = i
        if rowSums[i] < minRow and rowSums[i] > 0:
            minRow = rowSums[i]
            x = i

    # mamy 1. kandydata na spełnienie warunków zadania
    cand1 = maxCol/minRow
    result1 = x, y
    maxCol, minRow = float('inf'), float('-inf')

    # znajdź najmniejszą ujemną sumę kolumn i największą ujemnę sumę wierszy
    for i in range(n):
        if maxCol > colSums[i] and colSums[i] < 0:
            maxCol = colSums[i]
            x = i
        if minRow < rowSums[i] and rowSums[i] < 0:
            minRow = rowSums[i]
            y = i
    # mamy 2. kandydata na wynik
    cand2 = maxCol/minRow
    result2 = x,y

    # porównujemy kandydatów
    if cand1 >= cand2:
        return result1
    else:
        return result2

def sum_row(T, row):
    sum = 0
    for i in range(len(T)):
        sum += T[row][i]
    return sum
def sum_col(T, col):
    sum = 0
    for i in range(len(T)):
        sum += T[i][col]
    return sum

n = int(input())
T = [[randrange(-9,10) for _ in range(n)] for _ in range(n)]
print(checkT(T, n))
for i in range(n):
    for j in range(n):
        print(T[i][j], end=' ')
    print()