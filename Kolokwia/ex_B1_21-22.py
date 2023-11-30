def lookForLongest(T):
    n = len(T)
    T2 = [True for _ in range(n)]
    maxLen = 0
    for i in range(n-1):
        if T2[i]:
            length = 1
            for j in range(i+1, n, 1):
                if areTheyGood(T[i], T[j]):
                    length += 1
                    T2[j] = False
            maxLen = max(length, maxLen)
    return maxLen

def areTheyGood(a, b):
    ADigits = [0 for _ in range(4)]
    BDigits = [0 for _ in range(4)]

    while a != 0:
        ADigits[a % 4] += 1
        a //= 4
    while b != 0:
        BDigits[b % 4] += 1
        b //= 4
    for i in range(4):
        if (ADigits[i] == 0 and BDigits[i] != 0) or (ADigits[i] != 0 and BDigits[i] == 0):
            return False
    return True

T = [13, 4, 23, 18, 22, 33, 9, 57, 40, 107, 123]
print(lookForLongest(T))