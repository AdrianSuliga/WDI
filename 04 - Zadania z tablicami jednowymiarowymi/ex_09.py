def longestIncrSubSeq(T):
    pT, maxCnt, cnt, n = 1, 0, 1, len(T)
    #sprawdzaj T za pomocą wskaźnika pT
    while pT < n:
        # dopóki rozważany podciąg jest rosnący
        while T[pT] > T[pT - 1]:
            cnt += 1
            # jeżeli można bezpiecznie przejść do następnej komórki
            if pT + 1 < n: 
                pT += 1
            else: break
        if cnt > maxCnt:
            maxCnt = cnt
        cnt = 1
        pT += 1
    return maxCnt
#len = 12
T = [7, 9, 1, 2, 3, 10, 9]
print(longestIncrSubSeq(T))