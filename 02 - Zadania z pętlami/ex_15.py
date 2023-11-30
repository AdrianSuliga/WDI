from math import sqrt
expr = sqrt(0.5)
oldFact, fact = sqrt(0.5), 0
while fact != 1:
    fact = sqrt(0.5 + 0.5 * oldFact)
    oldFact = fact
    expr = expr * fact
print(2/expr)
