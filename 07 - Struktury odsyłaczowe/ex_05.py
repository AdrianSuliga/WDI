"""
Proszę napisać funkcję, która rozdziela elementy listy odsyłaczowej do 10 list, 
według ostatniej cyfry pola val. W drugim kroku powstałe listy należy połączyć w jedną listę odsyłaczową, która jest
posortowana niemalejąco według ostatniej cyfry pola val.
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
    def printList(p):
        while p is not None:
            print(p.val, "-> ", end='')
            p = p.next
        print(None)
    def breakAndSort(p):
        while p is not None:
            pass

l1 = Node.genList()
l1.printList()
l1.breakAndSort()