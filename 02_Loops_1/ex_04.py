def intSqrt(n):
    sum = 0
    oddNum = 1
    counter = 0
    while True:
        if sum + oddNum <= n:
            sum += oddNum
        else:
            break
        counter += 1
        oddNum += 2
    return counter

for i in range(1, 101, 1):
    print(intSqrt(i), i)