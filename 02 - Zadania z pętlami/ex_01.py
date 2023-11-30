fL = 1
fM = 1
fR = 0

while True:
    if fL == 1 and fM == 1:
        print(1,1,end=' ')

    fR = fL + fM

    if (fR < 1000000):
        print(fR, end=' ')
        fL = fM
        fM = fR
    else:
        break