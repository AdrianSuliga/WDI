"""
Punkt leżący na płaszczyźnie jest opisywany parą liczb typu float (x,y). Tablica T[N] zawiera
współrzędne N punktów leżących na płaszczyźnie. Punkty posiadają jednostkową masę. Proszę napisać funkcję,
która sprawdza czy istnieje niepusty podzbiór n punktów, gdzie n <= k oraz n jest wielokrotnością liczby
3, którego środek ciężkości leży w odległości mniejszej niż r od początku układu współrzędnych. Do funkcji
należy przekazać dokładnie 3 parametry: tablicę t, promień r, oraz ograniczenie k, funkcja powinna zwrócić
wartość typu bool.
"""
from random import uniform
def ex30(T:list, r:float, k:int):
    def rec(T:list, S:tuple, r:float, k:int, ind:int):
        n = len(S)
        if n % 3 == 0 and n <= k and massCenter(S) <= r: return True
        if ind == len(T) - 1: return False
        return rec(T, S + (T[ind + 1],), r, k, ind + 1) or rec(T, S, r, k, ind + 1)
    return rec(T, (), r, k, -1)

def massCenter(S):
    n = len(S)
    if n == 0: return float('inf')
    x, y  = 0, 0
    for i in range(n):
        x += S[i][0]
        y += S[i][1]
    x /= n
    y /= n
    return (x*x + y*y)**(0.5)

n = int(input("N="))
r = float(input("r="))
k = int(input("k="))
T = [(uniform(0,100), uniform(0,100)) for _ in range(n)]
print(ex30(T, r, k))
print(T)