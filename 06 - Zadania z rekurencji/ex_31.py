"""
Proszę napisać funkcję, która jako parametr otrzymuje liczbę naturalną i zwraca sumę iloczynów elementów 
wszystkich niepustych podzbiorów zbioru podzielników pierwszych tej liczby. Można założyć,
że liczba podzielników pierwszych nie przekracza 20, zatem w pierwszym etapie funkcja powinna wpisać 
podzielniki do tablicy pomocniczej. Przykład: 60 → [2, 3, 5] → 2 + 3 + 5 + 2 * 3 + 2 * 5 + 3 * 5 + 2 * 3 * 5 = 71
"""
def ex31(n):
    T = factors(n)
    def rec(T, product, ind):
        n = len(T)
        if ind == n - 1 and product != 1: return product
        elif ind == n - 1 and product == 1: return 0
        return rec(T, product*T[ind+1], ind + 1) + rec(T, product, ind + 1)
    return rec(T, 1, -1)

def factors(n):
    T = [0 for _ in range(20)]
    if n < 2: return []
    b, i = 2, 0
    while b <= n**(0.5):
        if n % b == 0:
            T[i] = b
            i += 1
        while n % b == 0:
            n //= b
        b += 1
    if n > 1:
        T[i] = n
    b, i = 0, 0
    for t in T:
        if t != 0: b += 1
    Res = [0 for _ in range(b)]
    for j in range(b):
        Res[j] = T[j]
    return Res

n = int(input("n="))
print(ex31(n))