def FibSubSeq(sum):
    Ll, L, Lr = 0, 0, 1
    Rl, R, Rr = 0, 0, 1
    SL, SR = 0, 0
    #Ll, L, Lr - zmienne przechowujące 3 kolejne wyrazy ciągu Fib w "tablicy lewej"
    #Rl, R, Rr - zmienne przechowujące 3 kolejne wyrazu ciągu Fib w "tablicy prawej"
    #SL, SR - suma wyrazów ciagu Fib z "tablic - lewej i prawej"
    while True: #pętla liczy najmniejszą sumę fib > sum
        if SR == 0:
            SR += 1
            if SR > sum:
                break
        if SR == sum: return True
        Rl = R
        R = Rr
        Rr = Rl + R
        if SR <= sum:
            SR += Rr
        else:
            break
    while True: #pętla liczy sumę ciągu fib mniejszą lub równą od SR dopóki nie spotka takiego wyrazu że SR - SL == sum
        if SL == 0:
            SL += 1
            if SR - SL == sum: #
                return True
        Ll = L
        L = Lr
        Lr = Ll + L 
        if SL <= SR:
            SL += Lr
        else:
            return False
        if SR - SL == sum:
            return True


for i in range(1, 101, 1):
    print(FibSubSeq(i), i)
