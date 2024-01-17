"""
Proszę napisać funkcję, która otrzymując jako parametr wskazujący na początek listy jed-
nokierunkowej, przenosi na początek listy te z nich, które mają parzystą ilość piątek w zapisie ósemkowym.
"""
class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
    def genList():
        e5 = Node(16, None)
        e4 = Node(141, e5)
        e3 = Node(69, e4)
        e2 = Node(68, e3)
        e1 = Node(5, e2)
        e0 = Node(4, e1)
        return e0
    def printList(p):
        while p is not None:
            print(p.val, "-> ", end='')
            p = p.next
        print(None)
    def checkNum(n):
        cnt = 0
        while n != 0:
            if n % 8 == 5:
                cnt += 1
            n //= 8
        if cnt % 2 == 0: return True
        else: return False
    def move(p):
        if p == None or p.next == None:
            return p
        s, q = p, p
        p = p.next
        while p is not None:
            if Node.checkNum(p.val):
                q.next = p.next
                p.next = s
                s = p
                p = q.next
            else:
                q = p
                p = p.next
        return s

l = Node.genList()
l.printList()
l.move().printList()