from random import randrange
def P(n):
    A = 0
    for _ in range(1000):
        T = [randrange(1, 366) for _ in range(n)]
        for i in range(n-1):
            flag = True
            for j in range(i+1, n):
                if T[i] == T[j]:
                    A += 1
                    flag = False
                    break
            if not flag: break
    return A/1000

for i in range(20, 51):
    print(P(i), i)