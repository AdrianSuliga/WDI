def nwd1(a, b):
    while(b!=0):
        if (b>a): b = b%a
        if (b==0): return a
        if (a>b): a = a%b
        if (a==0): return b
def nwd2(a,b):
    while b!=0:
        helper = b
        b = a%b
        a = helper
    return a
            

a = int(input("a="))
b = int(input("b="))


print("4 IFY: ", nwd1(a,b))
print("HELPER: ", nwd2(a,b))