"""
Proszę napisać funkcję, która otrzymując jako parametr wskazujący na początek listy jed-
nokierunkowej, usuwa z niej wszystkie elementy, w których wartość klucza w zapisie trójkowym ma większą
ilość jedynek niż dwójek.
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
        e0 = Node(4, e1)
        return e0
    def printList(p):
        while p is not None:
            print(p.val, "-> ", end='')
            p = p.next
        print(None)
    def removeSelected(p):
        if p == None or (p.next == None and Node.checkNum(p)):
            return None
        s, q = p, None
        while p is not None:
            if Node.checkNum(p.val) and q == None:
                p = p.next
                s = p
            elif Node.checkNum(p.val) and q != None:
                q.next = p.next
                p = p.next
            else:
                q = p
                p = p.next
        return s
                
        return s
    def checkNum(n):
        onesCnt, twosCnt = 0, 0
        while n != 0:
            if n % 3 == 2: twosCnt += 1
            if n % 3 == 1: onesCnt += 1
            n //= 3
        if onesCnt > twosCnt:
            return True
        else: return False

l = Node.genList()
l.printList()
l.removeSelected().printList()
