"""
Dany jest zbiór N liczb naturalnych umieszczony w tablicy T[N]. Proszę napisać funkcję,
która zwraca informację, czy jest możliwy podział zbioru N liczb na trzy podzbiory, tak aby w każdym
podzbiorze, łączna liczba jedynek użyta do zapisu elementów tego podzbioru w systemie dwójkowym była
jednakowa. Na przykład: [2, 3, 5, 7, 15] → true, bo podzbiory {2,7} {3,5} {15} wymagają użycia 4 jedynek,
[5, 7, 15] → f alse, podział nie istnieje
"""
def ex28(T):
    def rec(T, X, Y, Z, ind):
        if count1s(X) == count1s(Y) == count1s(Z) and X != (): return True
        if ind == len(T) - 1: return False
        return (rec(T, X + (T[ind + 1],), Y, Z, ind + 1) or rec(T, X, Y + (T[ind + 1],), Z, ind + 1) or
                rec(T, X, Y, Z + (T[ind + 1],), ind + 1) or rec(T, X, Y, Z, ind + 1))
    return rec(T, (), (), (), -1)

def count1s(set):
    cnt = 0
    for s in set:
        while s != 0:
            cnt += s % 2
            s //= 2
    return cnt

T = [2,3,5,7,15]
print(ex28(T))