def checkT(T, n):
    maxL, L, sumI, sum = 0, 1, 0, 0
    it = 0
    while it < n-1:
        sumI = it
        sum = T[it]
        while T[it+1] > T[it]:
            L += 1
            sumI += it+1
            sum += T[it+1]
            if it+1 < n-1: it += 1
            else: break
        if sumI == sum:
            maxL = max(L, maxL)
        L = 1
        if it+1 < n-1: it += 1
        else: break
    return maxL

n = 12
T = [4, 1, 2, 3, 1, 1, 5, 2, 7, 8, 9, 19]
print(checkT(T,n))