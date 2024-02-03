def multiInFib(n):
    fibL = 1
    fibM = 1
    fibR = 2
    while True:
        if fibL * fibM == n:
            return True
        elif fibL * fibM > n:
            return False
        fibL = fibM
        fibM = fibR
        fibR = fibL + fibM

for i in range(1, 101, 1):
    print(multiInFib(i))