from math import log, floor
def checkNum(n):
    length = floor(log(n,10)) + 1
    while n != 0:
        if n % 10 == length:
            return True
        n //= 10
    return False

n = int(input("n="))
print(checkNum(n))