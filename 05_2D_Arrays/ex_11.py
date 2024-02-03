from random import randrange
def countNeighbours(T, n):
    cnt = 0
    moves = [(1,0), (-1,0), (0, 1), (0, -1)]
    for i in range(n):
        for j in range(n):
            legalMoves, tempCnt = 0, 0
            for move in moves:
                if -1 < i+move[0] < n and -1 < j+move[1] < n:
                    legalMoves += 1
            for move in moves:
                if -1 < i+move[0] < n and -1 < j+move[1] < n and areTheyFriends(T[i][j], T[i+move[0]][j+move[1]]):
                    tempCnt += 1
            if tempCnt == legalMoves:
                cnt += 1
    return cnt

def areTheyFriends(num1, num2):
    dig1 = [0 for _ in range(10)]
    dig2 = [0 for _ in range(10)]

    while num1 != 0:
        dig1[num1 % 10] += 1
        num1 //= 10
    while num2 != 0:
        dig2[num2 % 10] += 1
        num2 //= 10

    for i in range(10):
        if (dig1[i] == 0 and dig2[i] != 0) or (dig1[i] != 0 and dig2[i] == 0):
            return False
    return True

n = int(input())
#T = [[randrange(10,100) for _ in range(n)] for _ in range(n)]
T = [[343, 34, 43, 121],
     [11, 443, 12, 21],
     [90, 80, 10, 112],
     [1, 2, 3, 4]]
n=4
print(countNeighbours(T, n))
for i in range(n):
    for j in range(n):
        print(T[i][j], end=' ')
    print()
