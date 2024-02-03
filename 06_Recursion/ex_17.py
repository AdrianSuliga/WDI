"""
Dane są dwie liczby naturalne z których budujemy trzecią liczbę. W budowanej liczbie muszą wystąpić wszystkie 
cyfry występujące w liczbach wejściowych. Wzajemna kolejność cyfr każdej z liczb
wejściowych musi być zachowana. Na przykład mając liczby 123 i 75 możemy zbudować liczby 12375, 17523,
75123, 17253, itd. Proszę napisać funkcję która wyznaczy ile liczb pierwszych można zbudować z dwóch
zadanych liczb
"""
def build(num1, num2, res, i):
    if num1 == 0 and num2 == 0 and isPrime(res): 
        print(res)
        return 1
    elif num1 == 0 and num2 == 0:
        return 0
    cnt = 0
    if num1 != 0:
        cnt += build(num1 // 10, num2, res + (num1 % 10) * 10**i, i + 1)
    if num2 != 0:
        cnt += build(num1, num2 // 10, res + (num2 % 10) * 10**i, i + 1)
    return cnt

def isPrime(n):
    if n == 2: return True
    if n < 2 or n % 2 == 0: return False
    b = 3
    while b <= n**(0.5):
        if n % b == 0:
            return False
        b += 2
    return True

def ex17(n1, n2):
    return build(n1, n2, 0, 0)

n1 = int(input("n1 = "))
n2 = int(input("n2 = "))
print(ex17(n1, n2))