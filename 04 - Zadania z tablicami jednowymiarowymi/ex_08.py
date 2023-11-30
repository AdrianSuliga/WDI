from math import sqrt
def isItPrime(n):
    if n == 2: return True
    if n == 1 or n % 2 == 0: return False
    b = 3
    while b <= sqrt(n):
        if n % b == 0:
            return False
        b += 2
    return True

def check(T):
    n = len(T)
    T2 = [False for _ in range(n)]
    T2[0] = True

    for i in range(n):
        if T2[i]:
            k, temp = 2, T[i]
            while temp != 1:
                while temp % k == 0:
                    if i+k < n:
                        T2[i + k] = True
                    temp //= k
                while True:
                    k += 1
                    if isItPrime(k): break
    return T2[n-1]
    
# zaczynamy od T[0], 
T = [2, 7, 32, 11, 18, 19, 31, 4, 9]
print('\n',check(T))