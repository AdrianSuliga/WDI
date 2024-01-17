"""
Proszę napisać funkcję, która otrzymując jako parametr wskazujący na początek listy dwu-
kierunkowej, usuwa z niej wszystkie elementy, w których wartość klucza w zapisie binarnym ma nieparzystą
ilość jedynek.
"""
class Node:
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev
    def genList():
        e0 = e1 = e2 = e3 = e4 = Node(None)
        e4 = Node(19, None, e3)
        e3 = Node(5, e4, e2)
        e2 = Node(8, e3, e1)
        e1 = Node(31, e2, e0)
        e0 = Node(31, e1, None)
        return e0
    def printList(p):
        print(None, "-> ", end = '')
        while p is not None:
            print(p.val, "<-> ", end = '')
            p = p.next
        print(None)
    def remove(p):
        if p == None or (p.next == None and Node.check(p.val)):
            return None
        q, s = p, p
        p = p.next
        while p.next is not None:
            if q.prev == None and Node.check(q.val):
                p.prev = None
                q = p
                s = p
                p = p.next
            elif Node.check(p.val) and q.prev != None:
                q.next = p.next
                p = p.next
                p.prev = q
            else:
                q = p
                p = p.next
        if Node.check(p.val):
            q.next = None
        return s
    def check(n):
        cnt = 0
        while n != 0:
            cnt += n % 2
            n //= 2
        if cnt % 2 == 1:
            return True
        else: return False

l = Node.genList()
l.printList()
l.remove().printList()