class Node():
    def __init__(self, item) -> None:
        self.item = item
        self.next = None

class SinglyLinkedList():
    def __init__(self) -> None:
        self.head = None

    def addToFront(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
    

    def addToBack(self, item):
        newNode = Node(item)
        currentNode = self.head
        if not self.head:
            self.head = newNode
            return
        while currentNode.next:
            currentNode = currentNode.next
        currentNode.next = newNode

    def addToIndex(self, item, index):
        if not self.head and index == 0:
            self.head = Node(item)
            return
        if not self.head and index != 0:
            return 
        newNode = Node(item)
        currentNode = self.head
        for i in range (index - 1):
            if currentNode.next:
                currentNode = currentNode.next
                print(currentNode.item)
            else:
                print("out of bounds")
                return
        newNode.next = currentNode.next
        currentNode.next = newNode
        
    def delete(self, item):
        if not self.head:
            return False
        if self.head.item == item:
            self.head = self.head.next
            return True
        currentNode = self.head
        while currentNode.next and currentNode.next.item != item:
            currentNode = currentNode.next
        if currentNode.next:
            currentNode.next = currentNode.next.next
            return True
        return False

    def search(self, item):
        if not self.head:
            return False
        currentNode = self.head
        while currentNode:
            if currentNode.item == item:
                return True
            currentNode = currentNode.next
        return False




    def toList(self):
        ls = []
        if not self.head:
            return ls
        currentNode = self.head
        while currentNode:
            ls.append(currentNode.item)
            currentNode = currentNode.next
        return ls
        
if __name__ == "__main__":
    A = SinglyLinkedList()
    A.addToBack(1)
    A.addToBack(2)
    A.addToBack(3)
    A.addToBack(4)
    A.addToIndex(10, 5)
    print(A.toList())
