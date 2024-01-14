"""
Proszę napisać funkcję, która rozdziela elementy listy odsyłaczowej do 10 list, 
według ostatniej cyfry pola val. W drugim kroku powstałe listy należy połączyć w jedną listę odsyłaczową, która jest
posortowana niemalejąco według ostatniej cyfry pola val.
"""
class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
    def genList():
        e10 = Node(91, None)
        e9 = Node(88, e10)
        e8 = Node(31, e9)
        e7 = Node(12, e8)
        e6 = Node(66, e7)
        e5 = Node(103, e6)
        e4 = Node(505, e5)
        e3 = Node(74, e4)
        e2 = Node(7, e3)
        e1 = Node(209, e2)
        e0 = Node(147, e1)
        return e0
    def printList(p):
        while p is not None:
            print(p.val, "-> ", end='')
            p = p.next
        print(None)
    def breakAndSort(p):
        L = [None for _ in range(10)] # L[i] posłużymym się do tworzenie nowej listy
        S = [None for _ in range(10)] # S[i] przechowuje początek każdej z list
        while p is not None: # przechodzimy po początkowej liście i przepinamy odpowiednie elementy do nowych list
            for i in range(10):
                if p.val % 10 == i:
                    if L[i] == None: # przypadek początkowy, gdy lista nie istnieje jeszcze
                        L[i] = p
                        S[i] = L[i]
                    else:
                        L[i].next = p
                        L[i] = L[i].next
                    break
            p = p.next
        for i in range(10): # przepinamy większość ostatnich elementów nowych list do pierwszych elementów
            if L[i] is not None and i + 1 < 10: # list odpowiadających reszcie o 1 większej, wyjątkiem 
                L[i].next = S[i + 1] # jest lista odpowiadająca reszcie == 9
        L[9].next = None # przypadek końcowy, ostatnie element ostatniej listy przepinamy na None
        for i in range(10):
            if S[i] is not None:
                S[i].printList()
                break

l1 = Node.genList()
l1.printList()
l1.breakAndSort()