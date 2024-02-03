def DecToBase(n, base):
    result = [0] * n
    pos = 0
    while n != 0:
        if n % base >= 10:
            result[pos] = chr(n%base - 10 + ord('A'))
        else:
            result[pos] = n % base
        pos += 1
        n //= base
    for i in  range(pos-1,-1,-1):
        print(result[i],end='')

def main(n):
    for i in range(2, 17):
        DecToBase(n, i)
        print()

n = int(input("n="))
main(n)