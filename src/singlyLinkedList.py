class Node:
    def __init__(self, item) -> None:
        self.item = item
        self.next = None
    
class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def addToFront(self, item):
        newNode = Node(item)
        newNode.next = self.head
        self.head = newNode

    def toList(self):
        ret = []
        current = self.head
        while current:
            ret.append(current.item)
            current = current.next
        return ret

    def addToBack(self, item):
        newNode = Node(item)
        if not self.head:
            self.head = newNode
            # remember to return
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = newNode

    def delete(self, item):
        if not self.head:
            return False
        if self.head and self.head.item == item:
            self.head = self.head.next
            return True
        current = self.head
        while current.next:
            if current.next.item == item:
                current.next = current.next.next
                return True
            current = current.next
        return False
    
    def search(self, item):
        if not self.head:
            return False
        current = self.head
        while current:
            if current.item == item:
                return True
            current = current.next
        return False

    def addToIndex(self, item, index):
        # if not self.head and index != 0:
        #     return 
        newNode = Node(item)
        if index == 0:
            newNode.next = self.head
            self.head = newNode
            return
        current = self.head
        for i in range(index - 1):
            if not current.next:
                return
            current = current.next
        newNode.next = current.next
        current.next = newNode









if __name__ == "__main__":
    A = SinglyLinkedList()
    A.addToBack(1)
    A.addToBack(2)
    A.addToBack(3)
    A.addToBack(4)
    A.addToIndex(5, 2)
    print(A.toList())
