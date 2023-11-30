def lookForBiggest(n):
    L = digitCount(n)
    M, maxNum = 0, 0
    while n != 0:
        copy_n = n
        while copy_n != 0:
            if isPrime(copy_n) and differentDigits(copy_n):
                maxNum = max(maxNum, copy_n)
            copy_n //= 10
        M += 1
        n = n % (10**(L-M))
    return maxNum

def isPrime(n):
    if n == 2: return True
    if n < 2 or n % 2 == 0: return False
    b = 3
    while b <= n**(1/2):
        if n % b == 0:
            return False
        b += 2
    return True

def digitCount(n):
    cnt = 0
    while n != 0:
        cnt += 1
        n //= 10
    return cnt

def differentDigits(n):
    digits = [0 for _ in range(10)]
    while n != 0:
        digits[n % 10] += 1
        n //= 10
    for d in digits:
        if d > 1:
            return False
    return True

print(lookForBiggest(1202742516))