from random import randrange
def lookForSeq(T, n):
    pT, maxLenPos, maxLenNeg, cnt = 1, 0, 0, 2
    while pT < n:
        r = T[pT] - T[pT-1]
        if r > 0:
            if pT + 1 < n: pT += 1
            while T[pT] - T[pT - 1] == r:
                cnt += 1
                if pT + 1 < n: pT += 1
                else: break
            maxLenPos = max(maxLenPos, cnt)
            cnt = 2
            if pT == n-1: break
        elif r < 0:
            if pT + 1 < n: pT += 1
            while T[pT] - T[pT - 1] == r:
                cnt += 1
                if pT + 1 < n: pT += 1
                else: break
            maxLenNeg = max(maxLenNeg, cnt)
            cnt = 2
            if pT == n-1: break
        else: pT += 1
    return maxLenPos - maxLenNeg

n = int(input())
T = [randrange(1, 100) for _ in range(n)]
print(lookForSeq(T, n))
print(T)