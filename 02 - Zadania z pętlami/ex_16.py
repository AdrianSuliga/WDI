mS, mN = 0, 0
for i in range(2, 10001, 1):
    counter = 0
    cA = i
    while True:
        nA = (cA % 2) * (3*cA + 1) + (1 - cA%2) * cA // 2
        counter += 1
        cA = nA
        if nA == 1:
            if counter > mS:
                mS = counter
                mN = i
            break

print(mN, mS)
