"""
Dwie liczby są zgodne piątkowo, jeżeli posiadają tyle samo cyfr parzystych w ich reprezentacjach w systemie
pozycyjnym o podstawie 5. Dane są dwie tablice int tab1[MAX1][MAX1], tab2[MAX2][MAX2] (MAX2 > MAX1 > 1).
Proszę napisać funkcję, która sprawdzi, czy możliwe jest takie przyłożenie tab1 do tab2, aby w pokrywającym się
obszarze co najmniej 33% odpowiadających sobie elementów z tab1 i tab2 było zgodnych piątkowo. Uwaga: należy
uwzględnić, że tab1 może tylko częściowo przykrywać tab2 (patrz rysunek), a w sprawdzanym obszarze musi znaleźć
się co najmniej jeden element.
"""
from random import randrange
def searchArray(tab1, tab2): # przesuwamy tab1 nad tab2
    max1 = len(tab1)
    max2 = len(tab2)
    for i in range(-max1 + 1, max2): # zaczynamy od -max + 1, (i,j) przechowują współrzędne lewego-górnego rogu tab1
        for j in range(-max1 + 1, max2): # pętla przesuwa się tak, że zawsze tab1 pokrywa się częściowo z tab2
            if checkArrays(tab1, tab2, max1, max2, i, j): return True
    return False

def checkArrays(tab1, tab2, max1, max2, row, col): # sprawdza czy 33% lub więcej pól jest zgodne piątkowo
    cnt, commonArea = 0, 0
    for i in range(max1):
        for j in range(max1):
            if -1 < row + i < max2 and -1 < col + j < max2:
                commonArea += 1 # liczymy rozmiar wspólnej powierzchni
                if areTheyGood(tab1[i][j], tab2[i + row][j + col]):
                    cnt += 1 # liczymy ilość liczb zgodnych piątkowo
    if 3 * cnt / commonArea >= 1:
        return True
    else: return False

def areTheyGood(n1, n2): # sprawdź czy 2 liczby są zgodne piątkowo
    n1_5 = decTo5(n1)
    n2_5 = decTo5(n2)
    evenN1, evenN2 = 0, 0
    while n1_5 != 0:
        if n1_5 % 2 == 0: evenN1 += 1
        n1_5 //= 10
    while n2_5 != 0:
        if n2_5 % 2 == 0: evenN2 += 1
        n2_5 //= 10
    if evenN1 == evenN2: return True
    else: return False

def decTo5(n): # konwertuj liczbę dziesiętną na piątkową
    res, i = 0, 0
    while n != 0:
        res += (n % 5) * 10**i
        i += 1
        n //= 5
    return res

max1 = int(input())
max2 = int(input())
tab1 = [[randrange(1, 10) for _ in range(max1)] for _ in range(max1)]
tab2 = [[randrange(1, 10) for _ in range(max2)] for _ in range(max2)]
print(searchArray(tab1, tab2))
for i in range(max1):
    print(tab1[i])
for i in range(max2):
    print(tab2[i])