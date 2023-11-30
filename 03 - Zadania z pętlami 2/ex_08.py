def FibSubSeq(n):
    Ll, Lm, Lr = 0, 0, 1
    Rl, Rm, Rr = 0, 0, 1
    SR, SL = 0, 0
    #Sum SR:
    while True:
        if SR == 0:
            SR += 1
            if SR > n:
                break
        if SR == n: return True
        Rl = Rm
        Rm = Rr
        Rr = Rm + Rl
        if SR <= n:
            SR += Rr
        else:
            break
    #Sum SL:
    while True:
        if SL == 0:
            SL += 1
            if SR - SL == n:
                return True
        Ll = Lm
        Lm = Lr
        Lr = Lm + Ll
        if SL <= SR:
            SL += Lr
        else:
            return False
        if SR - SL == n:
            return True

n = int(input("n="))
n += 1
while True:
    if FibSubSeq(n):
        n += 1
    else:
        print(n)
        break