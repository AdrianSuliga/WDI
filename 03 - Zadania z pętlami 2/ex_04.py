def isIt235num(n):
    for i in [2,3,5]:
        while n % i == 0:
            n //= i
    if n == 1: return True
    else: return False

def howManyNums(n):
    counter = 0
    for i in range(1, n+1):
        if isIt235num(i): counter += 1
    return counter

print(howManyNums(12))
