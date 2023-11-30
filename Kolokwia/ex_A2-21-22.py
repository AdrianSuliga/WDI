def lookForBiggest(T):
    n = len(T)
    result, biggestNum = -1, 0
    for i in range(1, n):
        iloczyn = 1
        for j in range(i):
            if isPrime(T[j]):
                iloczyn *= T[j]
        if iloczyn == T[i]:
            biggestNum = max(biggestNum, iloczyn)
            result = i
    if result != -1:
        return result
    else: return None
def isPrime(n):
    if n == 2: return True
    if n < 2 or n % 2 == 0: return False
    b = 3
    while b <= n**(1/2):
        if n % b == 0:
            return False
        b += 2
    return True

T = [2, 3, 5, 6, 30, 1, 13, 7, 2730, 11, 23]
print(lookForBiggest(T))