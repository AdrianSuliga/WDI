# dodawanie pisemne, skoro liczymy e + 1/k! to nie musimy martwić się że wynik dodawania przekroczy rozmiary tablic
def addArrays(e, a, n):
    remains = 0
    for i in range(n-1, -1, -1):
        e[i] = e[i] + a[i] + remains
        remains = e[i]//10
        e[i] %= 10
    return e

# Funkcja główna, do drukowania e - zapisuje wynik dzielenia pisemnego z 1/k! dla wszystkich k takich że 1/k! !~ 0
# Następnie dodaje taką tablicę do obecnej wartości e, za pomocą dodawania pisemnego
def printE(n):
    e = [0] * n
    fact, l = 2, 1
    it = 3 
    while 1/fact != 0:
        tab = [0] * n
        # dzielenie pisemne, zapisuje do tab[] wartość 1/fact za pomocą dzielenia pisemnego
        # dla fact = 2; tab = [5, 0, 0, 0, ..., 0]
        # dla fact = 3; tab = [3, 3, 3, 3, ..., 3]
        for i in range(n):
            l = l * 10
            tab[i] = l // fact
            l = l % fact
        fact = fact * it
        it += 1
        l = 1
        # dodawanie pisemne e i tab
        addArrays(e, tab, n)
    print("2.",end='')
    for x in e:
        print(x,end='')

# Podaj dokładność
n = int(input("n="))
printE(n)