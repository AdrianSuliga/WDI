def decToBase(n, base):
    pos = 0
    arr = [0] * n
    # zapis do tablicy liczby n w odwrotnej kolejności niż poprawna
    # Przykład dla n = 72, base = 3
    # arr[0] = 72 % 3 = 0
    # n = 72//3 = 24
    # arr[1] = 24 % 3 = 0
    # n = 24//3 = 8
    # arr[2] = 8 % 3 = 2
    # n = 8 // 3 = 2
    # arr[3] = 2 % 3 = 2
    # arr = [0,0,2,2] podczas gdy (72)_{10} = (2200)_{3}
    while n != 0:
        if n % base >= 10:
            arr[pos] = chr(n % base + ord('A') - 10) 
        else:
            arr[pos] = n % base
        n //= base
        pos += 1
    # odwrócenie kolejności na poprawną
    for i in range(pos-1, -1, -1):
        print(arr[i],end='')

def decToBaseV2(n, base):
    result = ""
    while n != 0:
        if n % base >= 10:
            result = chr(n % base + ord('A') - 10) + result
        else:
            result = str(n % base) + result
        n //= base
    return result

n = int(input("decimal num: "))
#base = int(input("base (from 2 to 9): "))
#decToBase(n, base)
print()
#print(decToBaseV2(n, base))
for i in range(2, 17):
    print(decToBaseV2(n,i))