def findSeq(T):
    n = len(T[0])
    for i in range(n-2):
        for j in range(n-2):
            if T[i+2][j+2] + 1 == T[i][j] + T[i+1][j+1] and areTheyInSeq(T[i][j], T[i+1][j+1]):
                length = 3
                while -1 < i+length < n and -1 < j+length < n and T[i+length][j+length]+1==T[i+length-1][j+length-1]+T[i+length-2][j+length-2]:
                    length += 1
                return length

def areTheyInSeq(a, b):
    # 6, 9
    seqL, seqM, seqR = 1, 2, 2
    while True:
        if seqM == b and seqL == a: return True
        seqL = seqM
        seqM = seqR
        seqR = seqL + seqM - 1
        if seqL > a: return False

T = [[10, 9, 7, 5, 1], 
     [2, 3, 4, 8, 11], 
     [5, 2, 4, 20, 12], 
     [9, 8, 3, 5, 14], 
     [3, 2, 2, 5, 9]]
print(findSeq(T))