"""
Liczby naturalne reprezentowane jak poprzednim zadaniu. Proszę napisać funkcję dodającą
dwie takie liczby. W wyniku dodawania dwóch liczb powinna powstać nowa lista.
"""
class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
    def genList1():
        e5 = Node(9, None)
        e4 = Node(9, e5)
        e3 = Node(9, e4)
        e2 = Node(9, e3)
        e1 = Node(9, e2)
        e0 = Node(9, e1)
        return e0
    def genList2():
        e5 = Node(5, None)
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
    
    def addNums(p1, p2):
        res, p3 = 0, None
        p1 = Node.reverseList(p1)
        p2 = Node.reverseList(p2)

        while p1 is not None and p2 is not None:
            sum = p1.val + p2.val + res
            if p3 == None:
                p3 = Node(sum % 10, None)
                start = p3
            else:
                p3.next = Node(sum % 10, None)
                p3 = p3.next
            res = sum // 10
            p1 = p1.next
            p2 = p2.next

        while p1 is not None:
            sum = p1.val + res
            if p3 == None:
                p3 = Node(sum % 10, None)
                start = p3
            else:
                p3.next = Node(sum % 10, None)
                p3 = p3.next
            res = sum // 10
            p1 = p1.next
        while p2 is not None:
            sum = p2.val + res
            if p3 == None:
                p3 = Node(sum % 10, None)
                start = p3
            else:
                p3.next = Node(sum % 10, None)
                p3 = p3.next
            res = sum // 10
            p2 = p2.next

        if res != 0:
            p3.next = Node(res, None)
            p3 = p3.next
        
        return start.reverseList()

                
l1 = Node.genList1()
l2 = Node.genList2()
l1.printList()
l2.printList()
Node.addNums(l1, l2).printList()