from random import randrange
def checkMass(T, index, sum, target):
    if sum == target: return True
    if index == len(T) - 1: return False
    return checkMass(T, index + 1, sum + T[index + 1], target) or checkMass(T, index + 1, sum, target) or checkMass(T, index + 1, sum - T[index + 1], target)

def ex8(T, target):
    return checkMass(T, -1, 0, target)

n = int(input("n="))
target = int(input("target="))
T = [randrange(1,10) for _ in range(n)]
print(ex8(T, target))
print(T)