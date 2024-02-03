def DecToBase(n, base):
    result = [0] * n
    pos, pos2 = 0, 0
    while n != 0:
        result[pos] = n % base
        n //= base
        pos += 1
    reversedR = [0] * pos
    for i in range(pos-1, -1, -1):
        reversedR[pos2] = result[i]
        pos2 += 1
    return reversedR

def check(aInBase, bInBase, base):
    arrA = [0] * base
    arrB = [0] * base
    for x in aInBase:
        arrA[x] += 1
    for x in bInBase:
        arrB[x] += 1
    for i in range(0, base):
        if arrA[i] != 0 and arrB[i] != 0:
            return False
    return True

def main(a, b):
    for base in range(2, 17, 1):
        aInBase = DecToBase(a, base)
        bInBase = DecToBase(b, base)
        if check(aInBase, bInBase, base):
            return base

a = int(input("a="))
b = int(input("b="))
print(main(a,b))
