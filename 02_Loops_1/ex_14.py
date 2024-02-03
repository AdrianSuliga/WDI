from math import cos

x = float(input("x="))

cosinus = 1
i = 1
factor = 1

while factor != 0:
    factor = 1
    if i % 2 == 1: factor *= (-1)
    factorial = 1
    for j in range(1, 2*i+1, 1):
        factorial *= j
    factor = factor / factorial
    factor = factor * pow(x, i*2)
    cosinus += factor
    i += 1

print(cos(x))
print(cosinus)