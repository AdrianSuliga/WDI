def longestArithSubSeq(T):
    pT, maxCnt, cnt, n = 1, 0, 2, len(T)
    while pT < n-1:
        r = T[pT] - T[pT - 1]
        if pT + 1 < n: pT += 1
        while T[pT] - T[pT-1] == r:
            cnt += 1
            if pT + 1 < n:
                pT += 1
            else: break
        if cnt > maxCnt:
            maxCnt = cnt
        cnt = 2
    return maxCnt
        
T = [2, 4, 6, 8, 9, 10, 11, 12, 3, 6, 9]
print(longestArithSubSeq(T))