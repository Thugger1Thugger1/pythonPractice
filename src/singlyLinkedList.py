class Node():
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
        if not self.head:
            self.head = Node(item)
            return
        newNode = Node(item)
        current = self.head
        while current.next:
            current = current.next
        current.next = newNode
        
    def delete(self, item):
        current = self.head
        if not self.head:
            return False
        if current.item == item:
            self.head = current.next
            return True
        
        while current.next and current.next.item != item:
            current = current.next
        if current.next:
            current.next = current.next.next
            return True
        return False

    def search(self, item):
        current = self.head
        if not current:
            return False
        while current:
            if current.item == item:
                return True
            current = current.next
            
        return False

    def addToIndex(self, item, index):
        current = self.head
        newNode = Node(item)
        if not current:
            return
        if current.item == item and not current.next:
            newNode.next = self.head
            self.head = newNode
        for i in range(index - 1):
            current = current.next
        newNode.next = current.next
        current.next = newNode
        


if __name__ == "__main__":
    A = SinglyLinkedList()
    A.addToBack(1)
    A.addToBack(2)
    A.addToBack(3)
    A.addToBack(4)
    print(A.delete(1))
    print(A.toList())
