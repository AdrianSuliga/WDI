"""
Write a function, which deletes all non-unique elements from linked list. Function
should receive reference to the first element of a list
"""
class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next
    def genList():
        e6 = Node(4, None)
        e5 = Node(5, e6)
        e4 = Node(16, e5)
        e3 = Node(68, e4)
        e2 = Node(68, e3)
        e1 = Node(4, e2)
        e0 = Node(4, e1)
        return e0
    def printList(p):
        while p is not None:
            print(p.val, "-> ", end='')
            p = p.next
        print(None)
    def removeAllNonUnique(p):
        if p is None:
            return p
        prev, mStart = None, p
        while p is not None:
            listContainsEl = Node.contains(p, p.val)
            if listContainsEl and prev is not None:
                q, start = p, prev
                while q is not None:
                    if q.val == p.val:
                        prev.next = q.next
                        q = q.next
                    else:
                        prev = q
                        q = q.next
                p = start
            elif listContainsEl and prev is None:
                q, start = p, prev
                while q.val == p.val:
                    q = q.next
                    if q is None: return None
                start, prev = q, q
                q = q.next
                while q is not None:
                    if q.val == p.val:
                        prev.next = q.next
                        q = q.next
                    else:
                        prev = q
                        q = q.next
                p = start
                prev = None
                mStart = p
            else:
                prev = p
                p = p.next
        return mStart
    def contains(p, target):
        cnt = 0
        while p is not None:
            if p.val == target:
                cnt += 1
            p = p.next
        if cnt > 1:
            return True
        else: return False


l = Node.genList()
l.printList()
l.removeAllNonUnique().printList()
