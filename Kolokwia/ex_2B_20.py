"""
Dwie liczby są zgodne siódemkowo, jeżeli posiadają tyle samo cyfr nieparzystych w ich reprezentacjach w systemie
pozycyjnym o podstawie 7. Dane są dwie tablice int tab1[MAX1][MAX1], tab2[MAX2][MAX2] (MAX2 > MAX1 >= 1).
Proszę napisać funkcję, która sprawdzi, czy możliwe jest takie umieszczenie tab1 wewnątrz tab2, aby w
pokrywającym się obszarze co najmniej 33% odpowiadających sobie elementów z tab1 i tab2 było zgodnych
siódemkowo.
"""
from random import randrange
def search(tab1, tab2): # funkcja przesuwa lewy górny róg tablicy tab1 o wsp. (i,j) upewniając się że zawsze zawiera się ona
    max1, max2 = len(tab1), len(tab2) # w tab2
    for i in range(max2):
        for j in range(max2):
            if i + max1 < max2 and j + max1 < max2 and checkTabs(tab1, tab2, i, j): # jeżeli prawy, dolny róg się zawiera
                return (i,j) # w tab2, to całe tab1 się zawiera
    return False

def checkTabs(tab1, tab2, row, col): # sprawdź czy w tab1 i tab2 jest 33% liczb zgodnych siódemkowo
    max1, cnt = len(tab1), 0
    for i in range(max1):
        for j in range(max1):
            if areNumsGood(tab1[i][j], tab2[row + i][col + j]):
                cnt += 1
    if cnt / max1**2 >= 0.33: return True
    else: return False

def areNumsGood(num1, num2): # sprawdź czy 2 liczby są zgodne siódemkowo
    num1_7 = DecTo7Base(num1)
    num2_7 = DecTo7Base(num2) # postacie num1 i num2 w systemie siódemkowym
    oddNumsInN1, oddNumsInN2 = 0, 0
    while num1_7 != 0:
        if num1_7 % 2 == 1: oddNumsInN1 += 1
        num1_7 //= 10
    while num2_7 != 0:
        if num2_7 % 2 == 1: oddNumsInN2 += 1
        num2_7 //= 10
    if oddNumsInN1 == oddNumsInN2: return True
    else: return False

def DecTo7Base(n): # konwertuj liczbę dziesiętną na siódemkową
    res, it = 0, 0
    while n != 0:
        res += (n % 7) * 10**it
        n //= 7
        it += 1
    return res

max1 = int(input())
max2 = int(input())
tab1 = [[randrange(1, 10) for _ in range(max1)] for _ in range(max1)]
tab2 = [[randrange(1, 10) for _ in range(max2)] for _ in range(max2)]
print(search(tab1, tab2))
for i in range(max1):
    print(tab1[i])
for i in range(max2):
    print(tab2[i])