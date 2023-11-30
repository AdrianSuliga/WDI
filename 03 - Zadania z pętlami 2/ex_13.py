def checkNum(n):
    lastNum = n % 10
    n //= 10
    while n != 0:
        if n % 10 == lastNum:
            return False
        n //= 10
    return True    
# 21378

n = int(input("n="))
print(checkNum(n))