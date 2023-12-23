"""
W tablicy o rozmiarze N x N wypełnionej liczbami naturalnymi umieszczono dokładnie jeden fragment 
ciągu Fibonacciego o długości co najmniej 3 elementów. Cały fragment leży w jednym z wierszy
lub kolumn w kierunku rosnącym lub malejącym. Prosze napisać funkcję, która dla zadanej tablicy
odszuka ten fragment i zwróci jego wartość (długość?)
"""
def searchArray(T):
    n = len(T)
    for i in range(n - 2):
        for j in range(n - 2):
            if T[i][j] + T[i][j + 1] == T[i][j + 2]: # szukamy ciągu w wierszu w kolejności rosnącej
                cnt = 3
                while -1 < j + cnt < n and T[i][j + cnt] == T[i][j + cnt - 1] + T[i][j + cnt - 2]:
                    cnt += 1
                if isItInFibbonaci(T[i][j], T[i][j + 1]): return cnt
            if T[i][j] == T[i][j + 1] + T[i][j + 2]: # szukamy ciągu w wierszu w kolejności malejącej
                cnt = 3
                while -1 < j + cnt < n and T[i][j + cnt - 2] == T[i][j + cnt - 1] + T[i][j + cnt]:
                    cnt += 1
                if isItInFibbonaci(T[i][j + 1], T[i][j]): return cnt
            if T[i][j] + T[i + 1][j] == T[i + 2][j]: # szukamy ciągu w kolumnie w kolejności rosnącej
                cnt = 3
                while -1 < i + cnt < n and T[i + cnt][j] == T[i + cnt - 1][j] + T[i + cnt - 2][j]:
                    cnt += 1
                if isItInFibbonaci(T[i][j], T[i+1][j]): return cnt
            if T[i][j] == T[i][j + 1] + T[i][j + 2]: # szukamy ciągu w kolumnie w kolejnosci malejącej
                cnt = 3
                while -1 < i + cnt < n and T[i + cnt - 2] == T[i + cnt - 1][j] + T[i + cnt][j]:
                    cnt += 1
                if isItInFibbonaci(T[i + 1][j], T[i][j]): return cnt
    return 0   

def isItInFibbonaci(n1, n2): # sprawdzamy czy 2 liczby należą do ciągu Fib.
    fL, fM, fR = 0, 1, 1
    while True:
        if fM == n1 and fR == n2: return True
        if fR > n2: return False
        fL = fM
        fM = fR
        fR = fL + fM

n = 5
T = [[1, 0, 20, 7, 3],
     [1, 0, 13, 4, 5],
     [9, 8, 8, 5, 3],
     [2, 3, 5, 8, 5],
     [1, 1, 13, 1, 1]]
print(searchArray(T))