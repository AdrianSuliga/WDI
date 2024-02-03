"""
Na szachownicy o rozmiarach N × N reprezentowanej przez tablicę T[N][N] umieszczono pewną liczbę
wież szachowych tak, że każde z wolnych pól na szachownicy jest szachowane. Położenie wież w tablicy
oznaczono wartościami T rue. Przyszedł zły człowiek i zmienił położenie jednej z wież na szachownicy, tak że
nie wszystkie wolne pola są szachowane. Proszę zaproponować funkcję move(T), która znajdzie przeniesienie
jednej wieży, tak aby ponownie wszystkie pola były szachowane. Do funkcji przekazujemy tablicę T zawierającą 
położenie wież po zmianie położenia wieży. Funkcja powinna zwrócić dwa pola (wiersz, kolumna) –
skąd i dokąd należy przenieść wieżę
"""
def move(T):
    n = len(T)
    for i in range(n): # próbujemy przestawiać każdą znalezioną wieżę
        for j in range(n):
            if T[i][j]:
                for k in range(n):
                    for m in range(n):
                        if T[k][m]: continue # nie ma sensu zamieniać miejscami 2 wież
                        T[i][j] = 0 # pole gdzie przestawiamy wieżę musimy ustawić na True
                        T[k][m] = True
                        if checkT(T): return ((i,j), (k,m))
                        T[i][j] = True # po sprawdzeniu, odstawiamy wieżę
                        T[k][m] = 0
    return None # jeśli nie zwróciliśmy nic w pętlach to znaczy że żadnej wieży nie da się przestawić tak aby spełniała warunki zadania

def checkT(T): # funkcja sprawdza czy przy obecnym ułożeniu wież, wszystkie pola są szachowane
    n = len(T)
    for i in range(n):
        for j in range(n):
            if T[i][j]: # oznacz szachowane pola
                k = 1
                while -1 < i + k < n:
                    if T[i + k][j]: break
                    T[i + k][j] = None
                    k += 1
                k = 1
                while -1 < i - k < n:
                    if T[i - k][j]: break
                    T[i - k][j] = None
                    k += 1
                k = 1
                while -1 < j + k < n:
                    if T[i][j + k]: break
                    T[i][j + k] = None
                    k += 1
                k = 1
                while -1 < j - k < n:
                    if T[i][j - k]: break
                    T[i][j - k] = None
                    k += 1
                k = 1
    res = True
    for i in range(n):
        for j in range(n): # sprawdź czy wszystkie są szachowane
            if T[i][j] != None and not T[i][j]: res = False
    for i in range(n):
        for j in range(n):
            if T[i][j]: # odznacz szachowane pola
                k = 1
                while -1 < i + k < n:
                    if T[i + k][j]: break
                    T[i + k][j] = 0
                    k += 1
                k = 1
                while -1 < i - k < n:
                    if T[i - k][j]: break
                    T[i - k][j] = 0
                    k += 1
                k = 1
                while -1 < j + k < n:
                    if T[i][j + k]: break
                    T[i][j + k] = 0
                    k += 1
                k = 1
                while -1 < j - k < n:
                    if T[i][j - k]: break
                    T[i][j - k] = 0
                    k += 1
                k = 1
    return res

T = [[True, True, 0, 0],
     [0, True, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, True]]

print(move(T))
for i in range(4):
    print(T[i])
