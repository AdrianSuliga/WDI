end = None
def sequence(T):
    n = len(T)
    m = n // 2
    for i in range(3, m, 1):
        for j in range(i, n-i+1, 1):
            results = [0] * i
            for k in range(i):
                results[k] = T[j+k] / T[j-i+k]
            flaga = True
            for k in range(0, i-1, 1):
                if results[k] != results[k+1]:
                    flaga = False
            if flaga == True:
                print(j-i, j-1)
                return

sequence([3,2,5,7,3,2,3,5,7,6,9,15,21,17,19,23,2,6,4,8,3,5,7,1,3,2])
