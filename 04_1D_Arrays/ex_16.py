from random import randrange
def checkArray(t):
    n = len(t)
    maxT, minT = float('-inf'), float('inf')
    for i in range(n):
        if t[i] > maxT:
            maxT = t[i]
        if t[i] < minT:
            minT = t[i]
    cnt1, cnt2 = 0, 0
    for i in range(i):
        if t[i] == minT:
            cnt1 += 1
        if t[i] == maxT:
            cnt2 += 1
    if cnt1 > 1 or cnt2 > 1: return False
    return True

n = int(input())
t = [randrange(-99, 100) for _ in range(n)]
print(checkArray(t))
print(t)