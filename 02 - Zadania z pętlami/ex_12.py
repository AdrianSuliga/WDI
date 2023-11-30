a = int(input("a="))
b = int(input("b="))
c = int(input("c="))

while b != 0:
    helper = b
    b = a % b
    a = helper

while c != 0:
    helper = c
    c = a % c
    a = helper

print(a)
