def calcFraction(a, b, n):
    print(a//b, end='')
    print('.', end='')
    for i in range(n):
        a = a - b * (a//b)
        a = a * 10
        print(a//b, end='')
    print('')

calcFraction(113, 6, 101)
calcFraction(1221, 6, 101)