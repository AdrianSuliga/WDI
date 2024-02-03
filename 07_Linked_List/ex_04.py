"""
Proszę napisać funkcję, która dla podanej listy odsyłaczowej odwraca kolejność jej elementów.
"""
class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
    def genList():
        e5 = Node(11, None)
        e4 = Node(19, e5)
        e3 = Node(5, e4)
        e2 = Node(9, e3)
        e1 = Node(3, e2)
        return e1

def reverseList(p):
    if p == None or p.next == None: return p
    q, f = None, p.next
    while f is not None:
        p.next = q
        q = p
        p = f
        f = f.next
    p.next = q
    return p

def printList(p):
    while p is not None:
        print(p.val, "-> ", end = '')
        p = p.next
    print(None)

l1 = Node.genList()
printList(l1)
rl = reverseList(l1)
printList(rl)