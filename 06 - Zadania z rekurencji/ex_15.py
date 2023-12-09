# Problem 8 hetmanów
# =================================
# Należy rozstawić N hetmanów na zachownicy N na N tak aby żadne 2 się nie biły

# Funkcje znajdujące 1 rozwiązanie jeśli istnieje
def insertQueens(T, n, row):
    if row == n: return True
    for i in range(n):
        if canBePlaced(T, row, i):
            T[row][i] = 1
            if insertQueens(T, n, row + 1):
                return True
            T[row][i] = 0
    return False
def canBePlaced(T, row, col):
    n = len(T)
    for i in range(n):
        if T[row][i] == True: return False
        if T[i][col] == True: return False
        if -1 < row + i < n and -1 < col + i < n and T[row + i][col + i] == True: return False
        if -1 < row - i < n and  -1 < col - i < n and T[row - i][col - i] == True: return False
        if -1 < row + i < n and -1 < col - i < n and T[row + i][col - i] == True: return False
        if -1 < row - i < n and -1 < col + i < n and T[row - i][col + i] == True: return False
    return True

# Funkcja zliczająca wszystkie rozwiązania, brute force:
def countQueens(T, n, row):
    if row == n: return 1
    cnt = 0
    for i in range(n):
        if canBePlaced(T, row, i):
            T[row][i] = 1
            cnt += countQueens(T, n, row + 1)
            T[row][i] = 0
    return cnt

# Funkcja zliczająca wszystkie rozwiązania ale SZYBCIEJ, NA CHWAŁĘ DZIEKANAAA
# Jest tu też lepsza funkcja sprawdzająca czy się szachują
def countQueensV2(Q, ind, row, n):
    if row == n: return 1
    cnt = 0
    for col in range(n):
        flag = False
        for queen in Q:
            if doTheyCheck(queen, (row, col)):
                flag = True
                break
        if not flag:
            Q[ind] = (row, col)
            cnt += countQueensV2(Q, ind + 1, row + 1, n)
            Q[ind] = None
    return cnt
# h1, h2 to hetmany opisane za pomocą krotek (wiersz, kolumna)
def doTheyCheck(h1, h2):
    if h1 == None: return False
    if h1[0] == h2[0]: return True
    if h1[1] == h2[1]: return True
    if abs(h1[0] - h2[0]) == abs(h1[1] - h2[1]): return True
    return False

# main
def printT(T, n):
    for i in range(n):
        for j in range(n):
            print(T[i][j], end=' ')
        print()
def ex15(n):
    T = [[0 for _ in range(n)] for _ in range(n)]
    Q = [None for _ in range(n)]
    insertQueens(T, n, 0)
    #print(countQueens(T, n, 0))
    #print(countQueensV2(Q, 0, 0, n))
    printT(T, n)

n = int(input())
ex15(n)