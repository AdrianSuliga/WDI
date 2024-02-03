def insert(n):
    for i in range(0, 10):
        if n > biggestInput[i]:
            n, biggestInput[i] = biggestInput[i], n

biggestInput = [0] * 10
while True:
    n = int(input())
    if n == 0: break
    insert(n)
print(biggestInput[9])
