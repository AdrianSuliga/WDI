def sequence(T):
    maxF, minL = 0, float('inf')
    n = len(T)
    pT = 1
    while pT < n:
        length = 1
        while T[pT] > T[pT - 1]:
            length += 1
            if pT + 1 < n: pT += 1
            else: break
        if length > 2:
            maxF = max(maxF, T[pT-length])
            minL = min(minL, T[pT-1])
        if pT + 1 < n: pT += 1
        if pT == n-1: break
    if maxF > minL:
        return True
    else: return False

T = [2,15,17,13,17,19,23,2,6,4,8,3,5,7,1,3,2]
print(sequence(T))
T = [2,15,17,13,17,19,23,2,6,4,8,3,5,7,14,3,2]
print(sequence(T))