"""
Na zbiorze liczb całkowitych określono trzy operacje: A,B,C przekształcające liczby:
 A: zwiększa liczbę o 3;
 B: podwaja liczbę;
 C: wszystkie parzyste cyfry w liczbie zwiększa o 1, np. 2356->3357, 1999->1999.
Proszę napisać funkcję która sprawdza czy można przekształcić liczbę X na liczbę Y w nie więcej niż N krokach.
Do funkcji należy przekazać wartości X,Y,N, funkcja powinna zwrócić liczbę możliwych ciągów operacji
przekształcających liczbę X w Y (lub wartość 0 jeżeli takie przekształcenie nie istnieje). Uwaga: zabronione jest
używanie kolejno dwóch tych samych operacji
"""
from math import log10
def transform(X, Y, N): # w zmiennej bannedMove zakładamy, że 0 odpowiada A, 1 - B, 2 - C 
    def rec(X:int, Y:int, N:int, bannedMove:int, moves:int):
        if moves == N and X == Y:
            return 1
        elif moves == N and X != Y:
            return 0
        cnt = 0
        if bannedMove == 0: # jeżeli nie można wykonać A, to wykonujemy B i C i zapisujemy ile razy udało się
            cnt += rec(B(X), Y, N, 1, moves + 1) + rec(C(X), Y, N, 2, moves + 1) # stworzyć Y do zmiennej cnt
        elif bannedMove == 1:
            cnt += rec(A(X), Y, N, 0, moves + 1) + rec(C(X), Y, N, 2, moves + 1)
        elif bannedMove == 2:
            cnt += rec(A(X), Y, N, 0, moves + 1) + rec(B(X), Y, N, 1, moves + 1)
        else: # else będzie wywołany tylko w pierwszym wywołaniu rec, gdy bannedMove == -1
            cnt += rec(A(X), Y, N, 0, moves + 1) + rec(B(X), Y, N, 1, moves + 1) + rec(C(X), Y, N, 2, moves + 1)
        return cnt
    return rec(X, Y, N, -1, 0)

def A(num):
    return num + 3
def B(num):
    return num * 2
def C(num):
    size = int(log10(num) + 1)
    arr = [0 for _ in range(size)]
    it = size - 1
    while num != 0: # przepisanie cyfr liczby do tablicy
        arr[it] = num % 10
        num //= 10
        it -= 1
    for i in range(size): # inkrementacja parzystych liczb
        if arr[i] % 2 == 0: 
            arr[i] += 1
    result = 0
    it = size - 1
    for a in arr: # ponowna zamiana na liczbę
        result += a * 10**it
        it -= 1
    return result

print(transform(11,32,4))