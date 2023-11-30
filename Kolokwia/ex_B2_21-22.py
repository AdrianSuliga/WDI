from math import log10, floor
def isPrime(n):
    if n == 2: return True
    if n < 2 or n % 2 == 0: return False
    b = 3
    while b <= n**(1/2):
        if n % b == 0:
            return False
        b += 2
    return True

def rotate(n):
    lenN = floor(log10(n)) + 1
    digit = n // 10 ** (lenN-1)
    num = n % (10 ** (lenN-1)) 
    num *= 10
    return num+digit

def lookForBase(n):
    lenN = floor(log10(n)) + 1
    for base in range(2, 17):
        for _ in range(lenN):
            n = rotate(n)
            copyN = n
            product = 1
            while copyN > 0:
                product *= copyN % base
                copyN //= base
            if isPrime(product):
                return base
    return None 

n = int(input("n="))
print(lookForBase(n))
