def isItMulti(n):
    A = 2
    while True:
        if n % A == 0:
            return True
        if 3*A + 1 > n:
            return False
        A = 3*A + 1

for i in range(1, 101):
    print(isItMulti(i), i)
