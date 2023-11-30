from random import randrange
def placeSquare(T1, T2):
    n1, n2 = len(T1), len(T2)
    for i in range(n2):
        for j  in range(n2):
            if -1 < i + n1 < n2 and -1 < j + n1 < n2 and countGoodInT1(T1, n1)/n1**2 > 0.33:
                return True
    return False

def countGoodInT1(T1, n1):
    cnt = 0
    for i in range(n1):
        for j in range(n1):
            locaclCnt = 0
            for j in range(n1):
                for k in range(n1):
                    if areTheyGood(T1[j][k], T1[i][j]):
                        locaclCnt += 1
            if locaclCnt >= 2:
                cnt += 1
    return cnt

def areTheyGood(a, b):
    cntA, cntB = 0, 0
    while a != 0:
        if a % 2 == 1: cntA += 1
        a //= 2
    while b != 0:
        if b % 2 == 1: cntB += 1
        b //= 2
    if cntA == cntB: return True
    else: return False

n1 = int(input("n1="))
n2 = int(input("n2="))
if n2 >= n1:
    T1 = [[randrange(10, 100) for _ in range(n1)] for _ in range(n1)]
    T2 = [[randrange(10, 100) for _ in range(n2)] for _ in range(n2)]
    print(placeSquare(T1, T2))
else:
    print("ERROR")