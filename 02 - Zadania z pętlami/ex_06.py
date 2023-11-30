def bisectionRoot(n):
    upper, lower = 1, 1
    for i in range(1, n, 1):
        if n == 2 or n == 3:
            upper = 2
            break
        elif pow(i,i) > n:
            upper = pow(i-1, i-1)
            break
    for i in range(100):
        x = (upper+lower)/2
        if pow(x,x) == n:
            return x
        if (pow(lower,lower)-n) * (pow(x,x)-n) < 0:
            upper = x
        if (pow(upper,upper)-n) * (pow(x,x)-n) < 0:
            lower = x
    return x
    
print(bisectionRoot(2020))
