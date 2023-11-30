# A = {0, 1, }
# B = {2, 2, }
oldB = 2
oldA = 0
while True:
    a = int(input(""))
    if a == 0: break
    b = oldB + 2*oldA
    print(b)
    oldA = a
    oldB = b
