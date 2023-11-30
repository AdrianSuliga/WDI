def isArmstrongNum(num, p):
    sumP, oldNum = 0, num
    while num != 0:
        sumP += (num % 10) ** p
        num //= 10
    if sumP == oldNum: return True
    else: return False

n = int(input("n="))
"""
for j in range(1, 20):
    for i in range(10**(j-1), 10**j, 1):
        if isArmstrongNum(i, j): print(i)
"""
for i in range(10**(n-1), 10**n, 1):
        if isArmstrongNum(i, n): print(i)