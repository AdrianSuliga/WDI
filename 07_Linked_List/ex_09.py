"""
Dana jest niepusta lista reprezentująca liczbę naturalną. Kolejne elementy listy przechowują
kolejne cyfry. Proszę napisać funkcję zwiększającą taką liczbę o 1.
"""
class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
    def genList():
        e5 = Node(9, None)
        e4 = Node(9, e5)
        e3 = Node(9, e4)
        e2 = Node(9, e3)
        e1 = Node(9, e2)
        e0 = Node(9, e1)
        return e0
    def printList(p):
        while p is not None:
            print(p.val, "-> ", end='')
            p = p.next
        print(None)
    def reverseList(p):
        if p == None or p.next == None:
            return p
        q, f = None, p.next
        while f is not None:
            p.next = q
            q = p
            p = f
            f = f.next
        p.next = q
        return p
    def increment(p):
        if p == None: return p
        p = Node.reverseList(p)
        q, prev = p, p
        while p is not None and p.val == 9:
            p.val = 0
            prev = p
            p = p.next
        if p is not None:
            p.val += 1
            while p is not None:
                p = p.next
        else:
            prev.next = Node(1, None)
        return q.reverseList()

l = Node.genList()
l.printList()
l.increment().printList()