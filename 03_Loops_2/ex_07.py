# A_n = n*n + n + 1
def isItMulti(n):
    A = 1
    cnt = 1
    while A <= n:
        A = cnt*cnt + cnt + 1
        if n % A == 0:
            return True
        cnt += 1
    return False

n = int(input("n = "))
print(isItMulti(n))