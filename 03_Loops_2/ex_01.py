def checkNum(n):
    fibL, fibM, fibR = 1, 1, 0
    while True:
        if fibL * fibM == n:
            return True
        if fibL * fibM > n:
            return False
        fibR = fibL + fibM
        fibL = fibM
        fibM = fibR

for i in range(1, 101):
    print(checkNum(i), i)


