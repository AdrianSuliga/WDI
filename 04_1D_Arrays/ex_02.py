def check(a,b):
    arr = [0] * 10
    while a != 0:
        arr[a%10] += 1
        a //= 10
    while b != 0:
        arr[b%10] -= 1
        b //= 10
    for x in arr:
        if x != 0: return False
    return True

a = int(input("a="))
b = int(input("b="))
print(check(a,b))