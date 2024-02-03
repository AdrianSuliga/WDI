import math
def showDivisors(n):
    b = 1
    while b <= math.sqrt(n):
        if b == math.sqrt(n):
            print(b)
        elif n % b == 0:
            print(b, n//b)
        b += 1

for i in range(1, 101, 1):
    showDivisors(i)
    print('\n')