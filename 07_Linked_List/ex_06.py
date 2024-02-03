"""
Proszę napisać funkcję wstawiającą na koniec listy nowy element. Do funkcji należy przekazać
wskazanie na pierwszy element listy oraz wstawianą wartość.
"""
class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
    def genList():
        e10 = Node(91, None)
        e9 = Node(88, e10)
        e8 = Node(31, e9)
        e7 = Node(12, e8)
        e6 = Node(66, e7)
        e5 = Node(103, e6)
        e4 = Node(505, e5)
        e3 = Node(74, e4)
        e2 = Node(7, e3)
        e1 = Node(209, e2)
        e0 = Node(147, e1)
        return e0
    def append(p, iVal): # finally, dziekan approved append
        if p is None:
            return Node(iVal, None)
        q, s = None, p
        while p is not None:
            q = p
            p = p.next
        q.next = Node(iVal, None)
        return s
    def printList(p):
        while p is not None:
            print(p.val, "-> ", end='')
            p = p.next
        print(None)
    
l1 = Node.genList()
l1.printList()
l1.append(2137).printList()