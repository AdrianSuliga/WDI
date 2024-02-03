from math import log, floor

def constructNum(binaryNum, n, l):
    result = ""
    for i in range(l, 0, -1):
        if binaryNum[i-1] == '1':
            result = str(n % 10) + result
        n //= 10
    return result

def decToBin(n):
    result = ""
    while n != 0:
        result = str(n % 2) + result
        n //= 2
    return result
    
n = int(input("n="))
length = floor(log(n, 10)) + 1

for i in range(1, (2**length) - 1):
    iBin = decToBin(i)
    while len(iBin) != length:
        iBin = "0" + iBin
    result = int(constructNum(iBin, n, length))
    if result % 7 == 0:
        print(result)
    
