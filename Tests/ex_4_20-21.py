"""
Dana jest liczba naturalna N. Proszę zaimplementować funkcję divide(N), która sprawdza czy jest możliwe
pocięcie liczby N na kawałki, tak aby każdy z kawałków był liczba pierwszą oraz liczba kawałków też była
liczbą pierwszą. Funkcja powinna zwracać wartość logiczną. Na przykład: divide(2347)=True, podział na
23 i 47, natomiast divide(2255)=False.
"""
from math import log10
def divide(N):
    def rec(n, size):
        if n == 0 and isPrime(size): return True
        elif n == 0 and not isPrime(size): return False
        for i in range(1, int(log10(n)) + 2):
            if isPrime(n % 10**i) and rec(n // 10**i, size + 1):
                return True
        return False
    return rec(N, 0)

def isPrime(n):
    if n == 2: return True
    if n < 2 or n % 2 == 0: return False
    b = 3
    while b <= n**(0.5):
        if n % b == 0:
            return False
        b += 2
    return True

print(divide(2255))