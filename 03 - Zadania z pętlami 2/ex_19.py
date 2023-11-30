def printFraction(a,b):
    print(a // b, end = '')
    a = a % b
    if a != 0:
        print('.', end = '')
        for _ in range(calc2sAnd5s(b)):
            a = a * 10
            print(a//b, end = '')
            a = a % b
        if a != 0:
            print('(', end = '')
            reminder = a
            while True:
                a = a * 10
                print(a//b, end = '')
                a = a % b
                if a == reminder: break
            print(')')

def calc2sAnd5s(b):
    sum2, sum5 = 0, 0
    while b % 2 == 0:
        sum2 += 1
        b //= 2
    while b % 5 == 0:
        sum5 += 1
        b //= 5
    return max(sum2, sum5)

a = int(input("a="))
b = int(input("b="))
printFraction(a,b)