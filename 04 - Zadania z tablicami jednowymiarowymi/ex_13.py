from random import randrange
def lookForReverse(T, n):
    maxLen, len = 0, 2
    while len < n:
        for i in range(n-len+1):
            Seq = [0 for _ in range(len)]
            pSq = 0
            for j in range(i, i+len):
                Seq[pSq] = T[j]
                pSq += 1
            if containsSeq(T, n, Seq, len):
                maxLen = len
                break
        len += 1
    return maxLen

def containsSeq(T, n, S, k):
    flag = True
    for i in range(n-1, -1, -1):
        if T[i] == S[0] and i-k >= -1:
            pS = 0
            for j in range(i, i-k, -1):
                if T[j] != S[pS]: 
                    flag = False
                    break
                pS += 1
            if flag: return True
            flag = True
    return False

n = int(input())
#T = [2, 9, 3, 1, 7, 11, 9, 6, 7, 11, 7, 1, 3, 9, 12, 15, 9, 2]
T = [randrange(1, 10) for _ in range(n)]
print(lookForReverse(T, n))
print(T)