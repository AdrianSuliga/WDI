class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

def printList(head:Node):
    while head != None:
        print(head.val, "-> ", end='')
        head = head.next
    print("NONE")

def removeElement(ptr:Node, val:int):
    prev, first = None, ptr
    while ptr != None:
        if ptr.val == val and prev == None:
            return ptr.next
        elif ptr.val == val and prev != None:
            #prev.next = prev.next.next
            prev.next = ptr.next
            return first
        prev = ptr
        ptr = ptr.next
    return first

def addElement(ptr:Node, val:int):
    if ptr == None: return Node(val)
    prev, first = None, ptr
    while ptr != None:
        prev = ptr
        ptr = ptr.next
    prev.next = Node(val)
    return first

n1 = Node(10, None)
n2 = Node(34, n1)
n3 = Node(89, n2)
n4 = Node(51, n3)

printList(n4)
l = addElement(n4, 19)
printList(l)


# removing element from list
# l = removeElement(n4, 34)
# printList(l)
