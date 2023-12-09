"""
W szachownicy o wymiarach 8x8 każdemu z pól przypisano liczbę naturalną. Na ruchy króla
nałożono dwa ograniczenia: król może przesunąć się na jedno z 8 sąsiednich pól jeżeli ostatnia cyfra liczby na
polu na którym stoi jest mniejsza od pierwszej cyfry liczby pola docelowego, oraz w drodze do obranego celu
(np. narożnika) król nie może wykonać ruchu, który powoduje oddalenie go od celu. Dana jest globalna tablica
T[8][8] wypełniona liczbami naturalnymi reprezentująca szachownicę. Lewy górny narożnik ma współrzędne
w=0 i k=0. Proszę napisać funkcję sprawdzającą czy król może dostać się z pola w,k do prawego dolnego
narożnika.
"""
from random import randrange
def king(w, k, T):
    n = len(T)
    if w == n - 1 and k == n - 1: return True
    if w >= n or k >= n: return False

    k1, k2, k3 = False, False, False

    if -1 < w + 1 < n and -1 < k < n and canMove(T[w][k], T[w + 1][k]): k1 = king(w + 1, k, T)
    if -1 < w < n and -1 < k + 1 < n and canMove(T[w][k], T[w][k + 1]): k2 = king(w, k + 1, T)
    if -1 < w + 1 < n and -1 < k + 1 < n and canMove(T[w][k], T[w + 1][k + 1]): k3 = king(w + 1, k + 1, T)

    return k1 or k2 or k3

def canMove(n1, n2):
    x1 = n1 % 10
    x2 = 0
    while n2 != 0:
        x2 = n2 % 10
        n2 //= 10
    if x1 < x2: return True
    return False

n = int(input("n="))
T = [[randrange(10,100) for _ in range(n)] for _ in range(n)]
print(king(0, 0, T))
for i in range(n):
    print(T[i])