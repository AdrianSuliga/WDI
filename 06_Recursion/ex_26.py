# Do budowy liczby naturalnej reprezentowanej w systemie dwójkowym możemy użyć A cyfr
# 1 oraz B cyfr 0, gdzie A, B > 0. Proszę napisać funkcję, która dla zadanych parametrów A i B zwraca ilość
# wszystkich możliwych do zbudowania liczb, takich że pierwsza cyfra w systemie dwójkowym (najstarszy
# bit) jest równa 1, a zbudowana liczba jest złożona. Na przykład dla A=2, B=3 ilość liczb wynosi 3, są to
# 10010(2), 10100(2), 11000(2)
def build(a, b):
    def rec(a, b, res):
        if a == 0 and b == 0 and isComplex(binToDec(res)): return 1
        if a < 0 or b < 0: return 0
        return rec(a - 1, b, res + "1") + rec(a, b - 1, res + "0")
    print(rec(a - 1, b, "1"))

def isComplex(n):
    if n <= 2: return False
    if n % 2 == 0: return True
    b = 3
    while b <= n**(0.5):
        if n % b == 0:
            return True
        b += 2
    return False

def binToDec(s):
    res = 0
    b = 0
    for i in range(len(s) - 1, -1, -1):
        res = res + int(s[i]) * 2**b
        b += 1
    return res

a = int(input("a="))
b = int(input("b="))
build(a, b)