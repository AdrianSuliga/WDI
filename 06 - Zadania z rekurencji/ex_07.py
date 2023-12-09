#Dany jest zestaw odważników T[N]. Napisać funkcję, która sprawdza czy jest możliwe odważenie określonej masy. 
#Odważniki można umieszczać tylko na jednej szalce.
from random import randrange
def checkMass(T, index, sum, target):
    if sum == target: return True
    if index == len(T)-1: return False
    return checkMass(T, index + 1, sum + T[index + 1], target) or checkMass(T, index + 1, sum, target)

def ex7(T, target):
    return checkMass(T, -1, 0, target)

n = int(input("n = "))
T = [randrange(1,10) for _ in range(n)]
target = int(input("target = "))
print(ex7(T, target))
print(T)