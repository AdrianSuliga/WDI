from random import randrange
def longestPalindrome(T, n):
    maxP, cnt = 0, 1
    left, right = 1, 1
    # look for odd palindromes
    for i in range(1, n-1):
        if T[i] % 2 == 1:
            while -1 < i-left < n and -1 < i+right < n and T[i-left] == T[i+right] and T[i-left] % 2 == 1 and T[i+right] % 2 == 1:
                cnt += 2
                left += 1
                right += 1
            maxP = max(maxP, cnt)
            cnt, left, right = 1, 1, 1
    # look for even palindromes
    for i in range(0, n-1):
        if T[i] == T[i+1] and T[i] % 2 == 1:
            cnt, left, right = 2, 1, 2
            while -1 < i-left < n and -1 < i+right < n and T[i-left] == T[i+right] and T[i-left] % 2 == 1 and T[i+right] % 2 == 1:
                cnt += 2
                left += 1
                right += 1
            maxP = max(maxP, cnt)

    if maxP < 2: return 0
    else: return maxP
        
n = int(input())
T = [randrange(1, 10) for _ in range(n)]
print(longestPalindrome(T,n))
print(T)