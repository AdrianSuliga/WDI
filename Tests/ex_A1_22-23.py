def sequence(T):
    n = len(T)
    maxLen = n // 2
    for i in range(n):
        for j in range(3, maxLen):
                divisions = [0 for _ in range(j)]
                for k in range(j):
                    divisions[k] = T[j+i+k]/T[i+k]
                flag = True
                for k in range(j-1):
                    if divisions[k] != divisions[k+1]:
                        flag = False
                if flag: return(i,i+j-1)
            
T = [5,7,3,2,3,5,7,6,9,15,21,17,19,23,2,6,4,8,3,1,3,2]
print(sequence(T))