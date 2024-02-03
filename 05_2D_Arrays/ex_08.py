def lookForGeo(T, n):
    maxL = 0
    for i in range(n):
        for j in range(n):
            leng, k = 2, 0
            while i+k < n-2 and j+k < n-2:
                q = T[i+k+1][j+k+1] / T[i+k][j+k]
                if T[i+k+2][j+k+2] / T[i+k+1][j+k+1] == q:
                    leng += 1
                    k += 1
                else: break
            if maxL < leng:
                maxL = leng
    if maxL < 3:
        return False
    else:
        return True, maxL

n = 4
T = [[3, 3, 7, 9],
     [11, 4, 21, 1],
     [2, 9, 9, 8],
     [22, 13, 90, 27]]
print(lookForGeo(T, n))