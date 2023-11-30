from math import log
def calcRoot():
    x = 3
    e = eConst()
    while abs(x**x-2020) > 0.000000001:
        x = x - f(x)/df(x,e) 
    return x

def eConst():
    fact, e, it = 1, 1, 1
    while 1/fact > 0:
        fact *= it
        e += 1/fact
        it += 1
    return e

def f(x):
    return x**x-2020

def df(x,e):
    return x**x * log(x,e) + x**x

print(calcRoot())


