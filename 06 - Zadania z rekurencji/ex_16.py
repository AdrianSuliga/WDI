# Wyrazy budowane są z liter a..z. Dwa wyrazy ”ważą” tyle samo jeżeli: mają tę samą liczbę samogłosek oraz 
# sumy kodów ascii liter z których są zbudowane są identyczne, na przykład ula → 117, 108, 97
# oraz exe → 101, 120, 101. Proszę napisać funkcję wyraz(s1,s2), która sprawdza czy jest możliwe zbudowanie 
# wyrazu z podzbioru liter zawartych w s2 ważącego tyle co wyraz s1. Dodatkowo funkcja powinna wypisać
# znaleziony wyraz.
def build(s1, s2, res, ind):
    if asciiSum(res) == asciiSum(s1) and samo(res) == samo(s1):
        return True
    if ind  == len(s2) - 1: return False
    return build(s1, s2, res + s1[ind + 1], ind + 1) or build(s1, s2, res, ind + 1)

def asciiSum(s):
    res = 0
    for char in s:
        res += ord(char)
    return res

def samo(s):
    res = 0
    for char in s:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            res += 1
    return res

def ex16(s1, s2):
    return build(s1, s2, "", -1)

s1 = str(input())
s2 = str(input())
print(ex16(s1, s2))