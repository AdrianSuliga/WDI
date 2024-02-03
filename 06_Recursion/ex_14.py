# Problem wież Hanoi
def hanoi(n, A, B, C):
    if n == 0: return
    hanoi(n - 1, A, C, B)
    print(A, "->", C)
    hanoi(n - 1, B, A, C)

def ex14(n):
    hanoi(n, 'A', 'B', 'C')

n = int(input())
ex14(n)

