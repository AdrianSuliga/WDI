fstVal, sndVal = 1, 1
for j in range(10):
    fibL, fibM, fibR = fstVal, sndVal, 2
    for i in range(50):
        fibL = fibM
        fibM = fibR
        fibR = fibL + fibM
    print(fibR/fibM)
    sndVal+=3
    fstVal+=1