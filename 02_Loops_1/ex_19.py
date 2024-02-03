eulerConst = 0
factorial = 1
b = 0
while 1/factorial != 0:
    factorial = factorial * b
    if b == 0 or b == 1:
        factorial = 1
    eulerConst += 1/factorial
    b += 1
    print(eulerConst)
print(eulerConst)
    