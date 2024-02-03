# 1<2<3<4
def isItIncreasing(n):
    l = 10
    while n != 0:
        num = n % 10
        if num >= l:
            return False
        else:
            l = num
        n //= 10
    return True

n = int(input("n="))
print(isItIncreasing(n))