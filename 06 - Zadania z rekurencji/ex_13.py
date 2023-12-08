#Napisać program wypisujący wszystkie możliwe podziały liczby naturalnej na sumę składników.
#Na przykład dla liczby 4 są to: 1+3, 1+1+2, 1+1+1+1, 2+2
def printElements(n, res, p):
    if n == 0: print(res[1:])
    for i in range(p, n + 1):
        printElements(n - i, res + '+' + str(i), i)

def ex13(n):
    printElements(n, "", 1)

n = int(input())
ex13(n)