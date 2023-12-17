class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

def printList(head:Node):
    while head != None:
        print(head.val, "-> ", end='')
        head = head.next
    print("END")

def remove(ptr:Node, val:int):
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

n1 = Node(10)
n2 = Node(34, n1)
n3 = Node(89, n2)
n4 = Node(51, n3)
printList(n4)
a = remove(n4, 89)
printList(a)
