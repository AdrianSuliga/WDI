"""
Zastosowanie listy odsyłaczowej do implementacji tablicy rzadkiej. Proszę napisać trzy funkcje:
– inicjalizującą tablicę, – zwracającą wartość elementu o indeksie n, – podstawiającą wartość value pod indeks n
"""
from random import randrange
class Node:
    def __init__(self, ind, val, next = None):
        self.ind = ind
        self.next = next
        self.val = val

# ind = 6
# (1, 7) -> (2, 5) -> (5, 9) -> (9, 2) -> None
#                      prev     first
def insertEl(head, value, n):
    if head == None:
        return Node(n, value, None)
    first = head
    prev = None
    while first != None:
        if first.ind > n:
            nNode = Node(n, value, first)
            if prev is None:
                return nNode
            else: 
                prev.next = nNode
                return head
        elif first.ind == n:
            first.val = value
            return head
        prev = first
        first = first.next
    prev.next = Node(n, value, None)
    return head

def getVal(head, ind):
    while head != None:
        if head.ind == ind:
            return head.val    
        head = head.next
    return None

def createList():
    n4 = Node(9, 2, None)
    n3 = Node(5, 9, n4)
    n2 = Node(2, 5, n3)
    n1 = Node(1, 7, n2)
    return n1

def printList(head):
    while head != None:
        print(head.val, "->", end=' ')
        head = head.next
    print(None)

list = createList()
printList(insertEl(list, 13, 5))
