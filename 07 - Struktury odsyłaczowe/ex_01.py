# Zaimplementuj zbiór mnogościowy liczb naturalnych korzystając ze struktury listy odsyłaczowej.
# 1. czy element należy do zbioru
# 2. wstawienie elementu do zbioru
# 3. usunięcie elementu ze zbioru
class Node:
    def __init__(self, val:int, next = None):
        self.val = val
        self.next = next

def contains(head:Node, element:int):
    if head == None: return False
    while head != None:
        if head.val == element:
            return True
        head = head.next
    return False

def addElement(head:Node, element:int):
    if head == None: return Node(element)
    first, prev = head, None
    if contains(head, element): return first
    while head != None:
        prev = head
        head = head.next
    prev.next = Node(element)
    return first

def removeElement(head:Node, element:int):
    if not contains(head, element): return head
    first, prev = head, None
    while head != None:
        if prev == None and head.val == element:
            first = head.next
            return first
        elif head.val == element:
            prev.next = head.next
            return first
        prev = head
        head = head.next
    return -1

def printList(head:Node):
    while head != None:
        print(head.val, "-> ", end='')
        head = head.next
    print(None)

def genList():
    n5 = Node(19)
    n4 = Node(21, n5)
    n3 = Node(43, n4)
    n2 = Node(99, n3)
    n1 = Node(11, n2)
    return n1
"""
list = genList()
printList(list)

nList = addElement(list, 3)
printList(nList)

mList = removeElement(nList, 11)
printList(mList)
"""