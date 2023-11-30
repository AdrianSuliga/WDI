from random import randrange
def check(n):
    while n != 0:
        if (n%10) % 2 == 0:
            return False
        n //= 10
    return True

def fillWithRand(t, n):
    for i in range(n):
        t[i] = randrange(1, 1001)

def main(t, n):
    fillWithRand(t, n)
    for i in t:
        if check(i):
            return True
    return False
    
            

n = int(input())
t = [0] * n
print(main(t, n))