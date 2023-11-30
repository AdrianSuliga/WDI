def root3rd(n):
    if n == 0: return 0.0
    x = 1
    for i in range(50):
        x = 1/3 * (2*x + n/(x*x))
    return x

for i in range(101):
    print(root3rd(i))