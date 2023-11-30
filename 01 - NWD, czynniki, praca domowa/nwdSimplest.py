def nwd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

a = int(input("a="))
b = int(input("b="))
print(nwd(a,b))