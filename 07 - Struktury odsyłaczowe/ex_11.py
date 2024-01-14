"""
Lista zawiera niepowtarzające się elementy. Proszę napisać funkcję do której przekazujemy
wskaźnik na początek oraz wartość klucza. Jeżeli element o takim kluczu występuje w liście należy go usunąć
z listy. Jeżeli elementu o zadanym kluczu brak w liście należy element o takim kluczu wstawić do listy.
"""
class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
    def genList():
        e5 = Node(21, None)
        e4 = Node(7, e5)
        e3 = Node(10, e4)
        e2 = Node(13, e3)
        e1 = Node(5, e2)
        e0 = Node(19, e1)
        return e0
    def printList(p):
        while p is not None:
            print(p.val, "-> ", end='')
            p = p.next
        print(None)
    def lookIns(p, key):
        if p == None:
            return Node(key, None)
        s, q = p, None
        while p is not None:
            if p.val == key:
                return True
            q = p
            p = p.next
        q.next = Node(key, None)
        return s

l = Node.genList()
l.printList()
l.lookIns(16).printList()