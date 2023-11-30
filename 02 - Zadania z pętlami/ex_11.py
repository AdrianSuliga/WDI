from math import sqrt
import time
s = time.time()
m = 2
while m < 1000000:
    Sm = 1
    b = 2
    while b < sqrt(m):
        if m % b == 0:
            Sm += b + m//b
        b += 1
    if b == sqrt(m):
        Sm += b
    
    n = Sm
    if n > m:
        Sn = 1
        b = 2
        while b < sqrt(n):
            if n % b == 0:
                Sn += b + n//b
            b += 1
        if b == sqrt(n):
            Sn += b
        if Sn == m and Sm == n and m < 1000000 and n < 1000000:
            print(m, n)
    m += 1
e = time.time()
print(e-s)
