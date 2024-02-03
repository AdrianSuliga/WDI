from random import randrange
def generateProperSums(t1, t2, n):
    allSums = [0 for _ in range(3**n)]
    for i in range(3**n):
        maskedForm = DecToMaskForm(i, n)
        sum = 0
        for j in range(n):
            if maskedForm[j] == 2:
                sum += t1[j] + t2[j]
            elif maskedForm[j] == 1:
                sum += t2[j] 
            elif maskedForm[j] == 0:
                sum += t1[j]
        allSums[i] = sum
        removeDuplicates(allSums, 3**n)
    for sum in allSums:
        if isPrime(sum):
            print(sum,end=' ')
    print()

def removeDuplicates(T, length):
    for i in range(length-1):
        for j in range(i+1, length):
            if T[j] == T[i]:
                T[j] = 0

def DecToMaskForm(num, n):
    result = [0 for _ in range(n)]
    iterator = n-1
    while num != 0:
        result[iterator] = num % 3
        iterator -= 1
        num //= 3
    return result

def isPrime(n):
    if n == 2: return True
    if n < 2 or n % 2 == 0: return False
    b = 3
    while b <= n**(1/2):
        if n % b == 0:
            return False
        b += 2
    return True

n = int(input())
t1 = [randrange(1, 10) for _ in range(n)]
t2 = [randrange(1, 10) for _ in range(n)]
generateProperSums(t1, t2, n)
print(t1, t2)