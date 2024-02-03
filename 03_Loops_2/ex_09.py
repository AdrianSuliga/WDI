def areaSum(k):
    frac = 0.0001
    
    area = 0
    n = int((k-1) / frac)
    for i in range(1, n+1, 1):
        area += frac / (1+frac*i)
    return area

k = int(input("k="))
print(areaSum(k))