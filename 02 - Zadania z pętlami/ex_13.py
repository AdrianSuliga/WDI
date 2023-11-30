a = int(input("a="))
b = int(input("b="))
c = int(input("c="))

oldA = a
oldB = b
oldC = c

while b != 0:
    helper = b
    b = a%b
    a = helper 

d = oldA * oldB // a
oldD = d

while c != 0:
    helper = c
    c = d%c
    d = helper
    
print(oldD * oldC // d)