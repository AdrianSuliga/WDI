"""
Na szachownicy o wymiarach N × N umieszczono pewną liczbę pionków. Położenie pionków opisuje 
lista [(w0, k0),(w1, k1),(w2, k2), ...]. W lewym górnym rogu szachownicy (o współrzędnych 0, 0) znajduje się
wieża, która musi dotrzeć do prawego dolnego rogu szachownicy. Wieża może wykonywać ruchy w prawo lub
w dół szachownicy i nie może zbijać pionków. Proszę napisać funkcję rook(N,L), która zwróci minimalną
liczbę ruchów jakie musi wykonać wieża aby dotrzeć do celu. Do funkcji należy przekazać wyłącznie dwa
parametry: rozmiar szachownicy N oraz listę L zawierającą położenia pionków. Jeżeli dotarcie do celu nie
jest możliwe funkcja powinna zwrócić wartość None.
"""
def rook(N, L):
    def recursion(N, L, row, col, cnt):
        if row == N - 1 and col == N - 1: return cnt # jeżeli wieża dotarła to zwróć cnt
        if row >= N or col >= N: return float('inf') # jeżeli wyszliśmy poza szachownicę to zwróć inf
        minMoves = float('inf')
        flag = True # flaga pozwoli nam przerwać pętlę jeśli natrafimy na pionka
        for i in range(1, N):
            for pawn in L: # sprawdzamy czy ruch w prawo o i spowoduje uderzenie w pionka
                if col + i == pawn[1] and row == pawn[0]:
                    flag = False
                    break
            if flag: # jeśli nie to idziemy w prawo
                minMoves = min(recursion(N, L, row, col + i, cnt + 1), minMoves)
            else: # jeśli tak to przerywamy pętlę i ustawimy flagę do poczatkowej wartości
                flag = True
                break
        for i in range(1, N): # analogiczna pętla do powyższej tylko idziemy w dół o i
            for pawn in L:
                if row + i == pawn[0] and col == pawn[1]:
                    flag = False
                    break
            if flag:
                minMoves = min(recursion(N, L, row + i, col, cnt + 1), minMoves)
            else:
                flag = True
                break
        return minMoves
    return recursion(N, L, 0, 0, 0)
N = 5
L = [(0,3), (2,1), (2,4), (3,3), (4,0), (4,3)]
print(rook(N, L))
