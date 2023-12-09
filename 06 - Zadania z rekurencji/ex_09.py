#Poprzednie zadanie. Program powinien wypisywać wybrane odważniki
from random import randrange
def printMass(T, index, sum1, sum2, target):
    if abs(sum1 - sum2) == target: return True
    if index == len(T) - 1: return False

    if printMass(T, index + 1, sum1 + T[index + 1], sum2, target):
        print("P", T[index + 1])
        return True
    elif printMass(T, index + 1, sum1, sum2 + T[index + 1], target):
        print("L", T[index + 1])
        return True
    elif printMass(T, index + 1, sum1, sum2, target):
        print("N")
        return True

def ex9(T, target):
    return printMass(T, -1, 0, 0, target) 

n = int(input("n="))
target = int(input("target="))
T = [randrange(1, 10) for _ in range(n)]
ex9(T, target)
print('\n',T)