"""
Punkt leżący w przestrzeni jest opisywany trójką liczb typu float (x,y,z). Tablica T[N] zawiera
współrzędne N punktów leżących w przestrzeni. Punkty posiadają jednostkową masę. Proszę napisać funkcję,
która sprawdza czy istnieje podzbiór punktów liczący co najmniej 3 punkty, którego środek ciężkości leży w
odległości nie większej niż r od początku układu współrzędnych. Do funkcji należy przekazać tablicę T oraz
promień r, funkcja powinna zwrócić wartość typu bool
"""
from random import uniform
def check(T:list, r:float):
    def rec(T:list, S:tuple, r:float, ind:int):
        if len(S) >= 3 and mw(S) <= r: return True
        if ind == len(T) - 1: return False
        return rec(T, S + (T[ind + 1],), r, ind + 1) or rec(T, S, r, ind + 1)
    return rec(T, (), r, -1)

def mw(S:tuple):
    n = len(S)
    if n == 0: return float('inf')
    x1, y1, z1 = 0, 0, 0
    for i in range(n):
        x1 += S[i][0]
        y1 += S[i][1]
        z1 += S[i][2]
    x1 /= n
    y1 /= n
    z1 /= n
    return (x1**2 + y1**2 + z1**2)**(0.5)

n = int(input("n="))
r = float(input("f="))
T = [(uniform(0, 100), uniform(0, 100), uniform(0, 100)) for _ in range(n)]
print(check(T, r))
print(T)