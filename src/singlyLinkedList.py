class Node:
    def __init__(self, item) -> None:
        self.item = item
        self.next = None

class SinglyLinkedList():
    def __init__(self) -> None:
        self.head = None

    def addToFront(self, item):
        newNode = Node(item)
        newNode.next = self.head
        self.head = newNode

    def toList(self):
        ls = []
        current = self.head
        while current:
            ls.append(current.item)
            current = current.next
        return ls

    def addToBack(self, item):
        newNode = Node(item)
        current = self.head
        if not current:
            newNode.next = self.head
            self.head = newNode
            return
        while current.next:
            current = current.next
        current.next = newNode

    def delete(self, item):
        current = self.head
        if not current:
            return False
        if current.item == item:
            self.head = self.head.next
            return True

        while current.next:
            if current.next.item == item:
                current.next = current.next.next
                return True
            current = current.next
        return False
        
    def addToIndex(self, item, index):
        current = self.head
        newNode = Node(item)
        if not current and index != 0:
            return 
        if index == 0:
            newNode.next = self.head
            self.head = newNode
            return
        for i in range(index - 1):
            if not current.next:
                print('"out of range"')
                return
            current = current.next
        newNode.next = current.next
        current.next = newNode

    def search(self, item):
        current = self.head
        while current:
            if current.item == item:
                return True
            current = current.next
        return False







if __name__ == "__main__":
    A = SinglyLinkedList()
    A.addToBack(1)
    A.addToBack(2)
    # A.addToBack(3)
    # A.addToBack(4)
    A.addToIndex(1, 1)
    print(A.toList())
