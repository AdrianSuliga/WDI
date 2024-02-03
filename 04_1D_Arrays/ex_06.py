from random import randrange
def check(n):
    while n != 0:
        if (n%10) % 2 == 1:
            return True
        n //= 10
    return False

def fillWithRand(t, n):
    for x in range(n):
        t[x] = randrange(1, 1001)
        print(t[x], end=' ')
    print()

def main(t, n):
    fillWithRand(t, n)
    for x in t:
        if not check(x):
            return False
    return True

n = int(input("n="))
t = [0] * n
print(main(t, n))