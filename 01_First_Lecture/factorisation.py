import math
def fact(n):
    b = 2
    while b <= math.sqrt(n):
        if n % b == 0:
            print(b, end=' ')
            n = n // b
        else:
            b = b + 1
    if (n>1): print(n)
#show only primes
x = int(input("Factorise: "))
fact(x)