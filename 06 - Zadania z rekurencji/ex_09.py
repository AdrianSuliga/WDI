from random import randrange
def printMass(T, index, sum, target):
    if sum == target: return True
    if index == len(T) - 1: return False

    

def ex9(T, target):
    return printMass(T, -1, 0, target) 

n = int(input("n="))
target = int(input("target="))
T = [randrange(1, 10) for _ in range(n)]
ex9(T, target)
print('\n',T)