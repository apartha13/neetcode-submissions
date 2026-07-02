class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def get(self, index: int) -> int:
        i = 0
        if index >= self.size:
            return -1
        curr = self.head
        while (i < index) and curr:
            curr = curr.next
            i += 1
        return curr.val

    def insertHead(self, val: int) -> None:
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
            self.size += 1
            return
        curr = self.head
        newNode.next = curr
        self.head = newNode
        self.size += 1

    def insertTail(self, val: int) -> None:
        newNode = Node(val)
        curr = self.head
        if curr == None:
            self.insertHead(val)
            return
        while curr.next:
            curr = curr.next
        curr.next = newNode
        self.size += 1

    def remove(self, index: int) -> bool:
        i = 0
        if index >= self.size:
            return False
        elif index == 0:
            self.head = self.head.next
            self.size -= 1
            return True
        curr = self.head
        prev = None
        while (i < index) and curr:
            prev = curr
            curr = curr.next
            i += 1
        prev.next = curr.next
        self.size -= 1
        self.print()
        return True
        

    def getValues(self) -> List[int]:
        curr = self.head
        arr = []
        if curr == None:
            return arr
        while curr:
            arr.append(curr.val)
            curr = curr.next
        return arr
    
    def print(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next
