# Tablica T = [(x1, y1),(x2, y2), ...] zawiera położenia N punktów o współrzędnych opisanych
# wartościami typu float. Proszę napisać funkcję, która zwróci najmniejszą odległość między środkami ciężkości
# 2 niepustych podzbiorów tego zbioru
def ex24(T):
    def rec(T, X1, X2, ind):
        n = len(T)
        if ind == n - 1:
            return sc(X1, X2)
        return min(rec(T, X1 + (T[ind + 1],), X2, ind + 1), rec(T, X1, X2 + (T[ind + 1],), ind + 1), rec(T, X1, X2, ind + 1))
    return rec(T, (), (), -1)
    
def sc(X1, X2):
    n1, n2 = len(X1), len(X2)
    if n1 == 0 or n2 == 0: return float('inf')
    x1, y1, x2, y2 = 0, 0, 0, 0
    for i in range(n1):
        x1 += X1[i][0]
        y1 += X1[i][1]
    x1 /= n1
    y1 /= n1
    for i in range(n2):
        x2 += X2[i][0]
        y2 += X2[i][1]
    x2 /= n2
    y2 /= n2
    return ((x2 - x1)**2 + (y2 - y1)**2)**(0.5)

T = [(1,1), (2,0), (1,-1)]
print(ex24(T))