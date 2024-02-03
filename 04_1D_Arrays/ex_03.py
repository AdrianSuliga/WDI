def genSieve(n):
    sieve = [True] * n
    sieve[0] = False
    sieve[1] = False
    for i in range(2, n):
        if sieve[i]:
            for j in range(i*i, n, i):
                sieve[j] = False
    return sieve

n = int(input("n="))
sieve = genSieve(n)
for i in range(1, n):
    if sieve[i]: print(i)