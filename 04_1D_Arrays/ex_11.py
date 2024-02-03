def longestGeoSubSeq(T):
    pT, maxCnt, cnt, n = 1, 0, 2, len(T)
    while pT < n-1:
        q = T[pT]/T[pT-1]
        if pT + 1 < n: pT += 1
        while abs(T[pT] / T[pT-1] - q) < 1e-10:
            cnt += 1
            if pT + 1 < n: pT += 1
            else: break
        if cnt > maxCnt:
            maxCnt = cnt
        cnt = 2
    return maxCnt

T = [128, 64, 32, 16, 8, 4, 2, 1]
print(longestGeoSubSeq(T))