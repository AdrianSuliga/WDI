from math import sqrt
def ex20(A, B):
    while abs(A-B) > 0.00000001:
        A, B = sqrt(A*B), (A+B)/2
    return A


print(ex20(15,10))