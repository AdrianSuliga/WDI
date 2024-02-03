startVal1, startVal2 = 1, 1
fibLeft = startVal1
fibMiddle = startVal2
fibRight = 0

while True:
    fibRight = fibLeft + fibMiddle
    if fibRight < 2023:
        fibLeft = fibMiddle
        fibMiddle = fibRight
    elif fibRight == 2023:
        print(startVal1, startVal2)
        break
    elif fibRight > 2023:
        startVal2 += 1
        fibLeft = startVal1
        fibMiddle = startVal2
        fibRight = 0     
