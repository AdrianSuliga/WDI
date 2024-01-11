"""
Proszę napisać funkcję scalającą dwie posortowane listy w jedną posortowaną listę. Do funkcji
należy przekazać wskazania na pierwsze elementy obu list, funkcja powinna zwrócić wskazanie do scalonej
listy. - funkcja iteracyjna, - funkcja rekurencyjna.
"""
class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def mergeSortedArr(head1, head2):
    if head1 == None: return head2
    if head2 == None: return head1
    start = None

    if head1.val <= head2.val:
        start = head1
        head1 = head1.next
    elif head1.val > head2.val:
        start = head2
        head2 = head2.next
    
    last = start

    while head1 is not None and head2 is not None:
        if head1.val <= head2.val:
            last.next = head1
            head1 = head1.next
        else:
            last.next = head2
            head2 = head2.next
        last = last.next

    while head1 is not None:
        last.next = head1
        last = last.next
        head1 = head1.next
    while head2 is not None:
        last.next = head2
        last = last.next
        head2 = head2.next

    return start

def printList(head):
    while head is not None:
        print(head.val, "-> ", end='')
        head = head.next
    print(None)

def initL1():
    n4 = Node(11, None)
    n3 = Node(9, n4)
    n2 = Node(3, n3)
    n1 = Node(1, n2)
    return n1
def initL2():
    n7 = Node(12, None)
    n6 = Node(11, n7)
    n5 = Node(10, n6)
    n4 = Node(8, n5)
    n3 = Node(7, n4)
    n2 = Node(4, n3)
    n1 = Node(2, n2)
    return n1

list1 = initL1()
list2 = initL2()
printList(mergeSortedArr(list1, list2))
