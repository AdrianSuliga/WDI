def longestT(T):
    n = len(T)
    longest, length = -float('inf'), 1
    for i in range(n-1):
        length = i + 1
        while checkSeq(T, i, length):
            if length + 1 < n: length += 1
            if length == n-1: break
        if not checkSeq(T, i, length):
            length -= 1
        longest = max(longest, length-i+1)
    return longest

def checkSeq(T, s, f):
    T2 = [0 for _ in range(1000)]
    for i in range(s, f+1):
        factors = factorise(T[i])
        for fact in factors:
            if fact != 0:
                T2[fact] += 1
    for t in T2:
        if t > 1: return False
    return True
    
def factorise(n):
    if n == 1: return []
    result = [0 for _ in range(1000)]
    it = 0
    b = 2
    while b <= n**(1/2):
        if n % b == 0:
            result[it] = b
            it += 1
            n //= b
        else: b += 1
    if n > 1:
        result[it] = n
        it += 1
    return result

t = [2, 23, 33, 35, 7, 4, 6, 7, 5, 11, 13, 17]
print(longestT(t))