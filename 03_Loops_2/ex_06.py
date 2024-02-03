from math import sqrt
def fact(n):
    if n == 0 or n == 1: return n,n
    smallest = 1, n
    b = 2
    while b < sqrt(n):
        if n % b == 0:
            smallest = b, n//b
        b += 1
    if b == sqrt(n):
        smallest = b, b
    return smallest

n = int(input("n="))
print(fact(n))