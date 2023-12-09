"""
Proszę napisać funkcję, która jako argument przyjmuje liczbę całkowitą i wypisuje wszystkie
co najmniej dwucyfrowe liczby pierwsze, powstałe poprzez wykreślenie z liczby pierwotnej co najmniej jednej
cyfry
"""
def crossNums(n, T):
    d = length(n)
    if d >= 2 and isPrime(n): 
        tryInsert(n, T)
        return
    elif d < 2: return
    for i in range(1, d + 1):
        copyN = n
        rem = copyN % 10**(i-1)
        copyN //= 10**i
        copyN = copyN*10**(i-1) + rem
        crossNums(copyN, T)

def ex1(n):
    T = [0 for _ in range(10**3)]
    crossNums(n, T)
    for t in T:
        if t != 0:
            print(t, end=' ')

def tryInsert(n, T):
    i = 0
    while T[i] != 0:
        if T[i] == n: return
        i += 1
    T[i] = n

def length(num):
    cnt = 0
    while num != 0:
        cnt += 1
        num //= 10
    return cnt

def isPrime(num):
    if num == 2: return True
    if num % 2 == 0 or num < 2: return False
    b = 3
    while b <= num**(0.5):
        if num % b == 0:
            return False
        b += 2
    return True

n = int(input("n="))
ex1(n)