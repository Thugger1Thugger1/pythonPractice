class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.last=None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def addToFront(self, value):
        NewNode = Node(value)
        if not self.head:
            self.head = self.tail = NewNode
            return 
        self.head.last = NewNode
        NewNode.next = self.head
        self.head = NewNode

    def addToBack(self, value):
        NewNode = Node(value)
        if not self.tail:
            self.head = self.tail = NewNode
            return 
        self.tail.next = NewNode
        NewNode.last = self.tail
        self.tail = NewNode


    def __str__(self) -> str:
        ret = []
        current = self.head
        while current:
            ret.append(current.value)
            current = current.next
        return str(ret)

    def toList(self) -> str:
        ret = []
        current = self.head
        while current:
            ret.append(current.value)
            current = current.next
        return ret

    def addToIndex(self, value, index):
        newNode = Node(value)
        if index == 0:
            self.addToFront(value)
            return
        current = self.head
        for i in range(index - 1):
            if not current.next:
                return
            current = current.next
        newNode = Node(value)
        newNode.next = current.next
        current.next = newNode
        newNode.last = current
        current.next.last = newNode

if __name__ == "__main__":

    a = DoublyLinkedList()
    a.addToFront(14)
    a.addToFront(15)
    a.addToFront(12)
    a.addToFront(10)
    a.addToIndex(0, 5)
    print(a)