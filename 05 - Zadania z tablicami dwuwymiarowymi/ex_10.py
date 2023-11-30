from random import randrange
def checkT(T, n):
    flag = False
    # sprawdź wiersze
    for i in range(n):
        for j in range(n):
            if T[i][j] == 0:
                flag = True
                break
        if not flag: return False
        flag = False
    # sprawdź kolumny
    for i in range(n):
        for j in range(n):
            if T[j][i] == 0:
                flag = True
                break
        if not flag: return False
        flag = False
    return True
    
n = int(input())
T = [[randrange(-9, 10) for _ in range(n)] for _ in range(n)]
print(checkT(T, n))
for i in range(n):
    for j in range(n):
        print(T[i][j],end='         ')
    print()