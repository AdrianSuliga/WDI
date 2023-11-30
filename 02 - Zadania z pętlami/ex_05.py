def newtonSqrt(n):
    x = 1
    for i in range(1, 21, 1):
        x = 0.5 * (x + n / x)
    return x

#x_{n+1} = 1/2 * (x_{n} + a / x_{n})
#i = 5
#x = 1
#x = 1/2 * (1 + 5/1) = 1/2 * 6 = 3
#x = 1/2 * (1 + 5/3) = 4/3 = 1.333333333333
#x = 1/2 * (1 + 15/4) = 2.375

for i in range(1, 101, 1):
    print(newtonSqrt(i), i)