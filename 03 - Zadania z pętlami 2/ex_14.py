from math import log, floor, sqrt
# check it there are a ones in binary form of n
def a1sInBin(a, binForm):
    cnt1 = 0
    for x in binForm:
        if x == 1: cnt1 += 1
    if cnt1 == a: return True
    else: return False

# take off binary mask from binForm
def takeOffMask(length, a, b, binForm):
    finalNum, cnt = 0, 0
    for x in binForm:
        if x == 0:
            finalNum += (b % 10) * 10**cnt
            b //= 10
        if x == 1:
            finalNum += (a % 10) * 10**cnt
            a //= 10
        cnt += 1
    return finalNum

# check if n is prime
def isItPrime(n):
    if n == 2: return True
    b = 3
    while b <= sqrt(n):
        if n % b == 0:
            return False
        b += 1
    return True

def genBinForm(n):
    result = [0] * n
    pos = 0
    while n != 0:
        result[pos] = n%2
        n //= 2
        pos += 1
    return result

# main function
def mainFunc(a, b):
    lenA, lenB = floor(log(a,10)) + 1, floor(log(b,10)) + 1
    n = lenA + lenB
    for i in range(2, 2**n, 1): # i in binary form represents all possible binary masks for numbers made by a and b
        binForm = genBinForm(i) # BINARY FORM IS REVERSED BUT IT DOES NOT MATTER IN OUR PROGRAM
        containsA1s = a1sInBin(lenA, binForm)
        if containsA1s:
            num = takeOffMask(n, a, b, binForm)
            if isItPrime(num):
                print(num)

a = int(input("a="))
b = int(input("b="))
mainFunc(a,b)
        