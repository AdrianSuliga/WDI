"""
Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy element listy o
wartościach typu int, usuwającą wszystkie elementy, których wartość jest mniejsza od wartości bezpośrednio
poprzedzających je elementów.
"""
class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
    def genList():
        e5 = Node("11", None)
        e4 = Node("32", e5)
        e3 = Node("43", e4)
        e2 = Node("11", e3)
        e1 = Node("14", e2)
        e0 = Node("12", e1)
        return e0
    def printList(p):
        while p is not None:
            print(p.val, "-> ", end='')
            p = p.next
        print(None)
    def removeSome(p):
        if p == None or p.next == None:
            return p
        s, f = p, p.next
        while f is not None:
            if p.val > f.val:
                p.next = f.next
                f = f.next
            else:
                p = f
                f = f.next
        return s

l = Node.genList()
l.printList()
l.removeSome().printList()
