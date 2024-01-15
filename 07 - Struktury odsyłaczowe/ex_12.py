"""
Zbiór mnogościowy zawierający napisy jest reprezentowany w postaci jednokierunkowej listy.
Napisy w łańcuchu są uporządkowane leksykograficznie. Proszę napisać stosowne definicje typów oraz funkcję
dodającą napis do zbioru. Do funkcji należy przekazać wskaźnik do listy oraz wstawiany napis, funkcja
powinna zwrócić wartość logiczną wskazującą, czy w wyniku operacji moc zbioru uległa zmianie.
"""
class Node:
    def __init__(self, val:str, next = None):
        self.val = val
        self.next = next
    def genList():
        e5 = Node("CA", None)
        e4 = Node("BB", e5)
        e3 = Node("BA", e4)
        e2 = Node("AC", e3)
        e1 = Node("AB", e2)
        e0 = Node("AA", e1)
        return e0
    def printList(p):
        while p is not None:
            print(p.val, "-> ", end='')
            p = p.next
        print(None)
    def addEl(p, el:str):
        if p == None:
            return Node(el, None)
        s, q = p, None
        while p is not None:
            if Node.isSmaller(p.val, el):
                if q == None:
                    nEl = Node(el, p)
                    return nEl
                nEl = Node(el, p)
                q.next = nEl
                return True
            if el == p.val:
                return False
            q = p
            p = p.next
        nEl = Node(el, None)
        q.next = nEl
        return True
    def isSmaller(s1:str, s2:str): # BA, AD
        n, i = min(len(s1), len(s2)), 0
        while i < n and s1[i] == s2[i]:
            i += 1
        if i == n:
            return False
        if ord(s1[i]) > ord(s2[i]):
            return True
        else: return False

l = Node.genList()
print(l.addEl("B").printList())