from math import log, floor
def isItPalindrome(num, base):
    length = floor(log(num, base)) + 1
    oldNum = num
    result = 0
    while num != 0:
        rem = num % base
        result += rem * pow(base, length - 1)
        num = num // base
        length -= 1
    if oldNum == result:
        return True
    else: return False
def checkIn10And2(n):
    print("In decimal system: ", isItPalindrome(n, 10))
    print("In binary system: ", isItPalindrome(n, 2))

checkIn10And2(119)