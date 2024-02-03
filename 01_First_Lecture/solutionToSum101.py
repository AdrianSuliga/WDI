from math import *
import time

# Generuje tabelę o rozmiarze size, na koniec działania funkcji
# w tabeli mamy True na liczbach pierwszych, False na złożonych.
# Funkcja wykorzystuje sito Eratostenesa
def sieve(size):
    a = [True] * size
    a[0] = False
    a[1] = False
    for i in range(size):
        if a[i]:
            for j in range(i*i, size, i):
                a[j] = False
    return a


def genPrimes(size):
    # krótka metoda na przerobienie wyniku sita na listę liczb pierwszych
    # nic szczególnego
    return [n for n,p in enumerate(sieve(size)) if p]


"""
Sedno algorytmu.
Generuje liczby z daną sumą cyfr, zaczynając od lewej.

W miarę typowy Depth First Search, polecam ogarnąć. Nie takie straszne jak się
wydaje.

e.g. jeśli generuję 8cyfrowe:
zaczynam od 1xxxxxxx
iteruję od 10xxxxxx do 19xxxxxx
kontynuuję z 2xxxxxxx
itd.

Pierwsza zaleta tego jest taka, że w każdej chwili znam aktualną sumę cyfr,
więc nie muszę jej liczyć dla każdej liczby.
O reszcie później.
"""

def dfs(pos, rem, base=0, primes=None):
    # generuję liczby pierwsze na później
    # pos = 10, rem = 90, base = 2.9 * 10**11, primes = [2, 3, ...]
    if primes == None:
        # primes == None implikuje że to nie jest rekurencyjne wywołanie
        # więc pos to długość liczb które generuję
        # generuję największe możliwe dzielniki
        # upper = 10^6 - generuje liczby do sqrt(10^pos) bo żadne liczby większe od tego pierwiastka nie będą czynnikami pierwszymi
        # rozważanych liczb
        upper = ceil(10**(pos/2))
        primes = genPrimes(upper) # primes = [2, 3, ...] - do 10^6
    """
    Ważny fragment.
    Sprawdzam czy:
    9 * ilość pozostałych cyfr < "niewykorzystana" suma  (101 - aktualna suma)

    Jeśli tak, nie starczy mi cyfr na dopełnienie sumy przy aktualnym prefiksie,
    więc mogę go pominąć. Zaoszczędza to *sporo* czasu.
    """
    # 
    if 9*pos < rem: # sprawdź czy pos-cyfrowa liczba złożona z 9 jest mniejsza od 101
        return False
    # rem = 101
    if rem < 0: # suma przekroczyła cel
        return False
    # pos = 12 
    if pos == 0: # uzupełniłem wszystkie cyfry
        assert rem == 0 # upewniam się że wykorzystałem całą sumę
        for p in primes: # sprawdzam czy jest pierwszą
            if base % p == 0:
                return None
        return base # jest
    # wstawiam w danym miejscu cyfry po kolei
    for d in range(10):
        r = dfs(pos=pos-1, rem=rem-d, base=base + d * 10**(pos-1), primes=primes)
        if r:
            return r
    return False

"""
Generując liczby "od lewej" muszę od początku znać długość.
Zaczynam od 1, jeśli nie znajdę żadnej o długości 1 generuję dłuższe aż do
skutku.

(niekoniecznie zbyt dobre rozwiązanie. algorytm się wyjebie jeśli target jest
podzielny przez trzy)
"""
def smallestPrimeDigitSum(target):
    i = 1
    while True:
        r = dfs(i, target)
        if r: return r
        i += 1

start = time.time()
print(smallestPrimeDigitSum(101))
end  = time.time()
print(end - start)