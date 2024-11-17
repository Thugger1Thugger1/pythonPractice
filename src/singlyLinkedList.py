class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class SinglyLinkedList():
    def __init__(self) -> None:
        self.head = None
        
    def add_to(self, data):
        """Add a new node to the end of the list."""
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            return
        # Traverse to the end of the list
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node  # Add the new node at the end
    
    def to_list(self):
        ls = []
        current = self.head
        while current:
            ls.append(current.data)
            current = current.next
        return ls

    def delete(self, data):
        if not self.head:  # If the list is empty
            return False
        if self.head.data == data:
            self.head = self.head.next
            return True
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        if current.next:
            current.next = current.next.next
            return True
        return False

    def search(self, data):
        if not self.head:  # If the list is empty
            return False
        if self.head.data == data:
            return True
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        if current.next:
            return True
        return False

if __name__ == "__main__":
    A = SinglyLinkedList()
    A.add_to(1)
    A.add_to(2)
    A.add_to(3)
    A.add_to(4)
    print(A.search(3))

