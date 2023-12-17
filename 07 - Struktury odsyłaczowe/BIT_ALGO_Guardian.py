class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next
    
def printList(head:Node):
    while head != None:
        print(head.val, "-> ", end='')
        head = head.next
    print("None")

def removeElement(ptr:Node, val:int):
    first = ptr
    while ptr != None:
        if ptr.next.val == val:
            ptr.next = ptr.next.next
            return first
        ptr = ptr.next
    return first

def addElement(ptr:Node, val:int):
    first = ptr
    while ptr.next != None:
        ptr = ptr.next
    ptr.next = Node(val)
    return first

d = Node(10)
c = Node(31, d)
b = Node(38, c)
a = Node(99, b)
g = Node(None, a)
"""
printList(g)
l = removeElement(g, 99)
printList(g)
"""
printList(a)
l = addElement(g, 7)
printList(a)