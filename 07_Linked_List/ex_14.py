"""
Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy element listy o
wartościach typu int, usuwającą wszystkie elementy, których wartość dzieli bez reszty wartość bezpośrednio
następujących po nich elementów.
"""
class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
    def genList():
        e5 = Node(16, None)
        e4 = Node(8, e5)
        e3 = Node(4, e4)
        e2 = Node(11, e3)
        e1 = Node(12, e2)
        e0 = Node(6, e1)
        return e0
    def printList(p):
        while p is not None:
            print(p.val, "-> ", end='')
            p = p.next
        print(None)
    def remove(p):
        if p == None or p.next == None:
            return p
        s, q, f = p, None, p.next
        while f is not None:
            if f.val % p.val == 0 and q == None:
                s = f
                p = f
            elif f.val % p.val == 0 and q is not None:
                q.next = f
                p = f
            else:
                q = p
                p = f
            f = f.next
        return s

l = Node.genList()
l.printList()
l.remove().printList()