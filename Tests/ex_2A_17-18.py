"""
Dana jest tablica int t[9], w której nale»y umie±ci¢ liczby od 1 do 9 tak, aby byªy speªnione warunki:
1) warto±ci na s¡siednich polach tablicy musz¡ si¦ ró»ni¢ o co najmniej 2
2) liczby pierwsze nie mog¡ zajmowa¢ s¡siednich pól tablicy
Warto±¢ 1 zostaªa ju» umieszczona w pierwszym (pod indeksem 0) elemencie tablicy. Prosz¦ napisa¢ program,
który wypisuje wszystkie poprawne rozmieszczenia liczb w tablicy.
"""
def insert(t):
    def rec(t, ind, prev, res):
        if ind == 9: 
            print(res)
            return
        for i in range(1, 10):
            if canPlace(i, prev):
                rec(t, ind + 1, i, res + str(i))
    return rec(t, 0, 1, "1")

def canPlace(numToPlace, prevNum):
    if isPrime(numToPlace) and isPrime(prevNum): return False
    if abs(numToPlace - prevNum) >= 2: return True
    return False

def isPrime(n):
    if n == 2: return True
    if n < 2 or n % 2 == 0: return False
    b = 3
    while b <= n**(0.5):
        if n % b == 0:
            return False
        b += 2
    return True

t = [0 for _ in range(9)]
t[0] = 1
insert(t)