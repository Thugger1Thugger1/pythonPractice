class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return (str(self.data))

class SinglyLinkedList():
    def __init__(self) -> None:
        self.head = None

    def add_to(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            print(current)
            current = current.next
        current.next = new_node

    def append_to_index(self, data, index):
        if not self.head and index != 0:
            return 
        if not self.head and index == 0:
            self.head = Node(data)
        current = self.head
        new_node = Node(data)
        for i in range(index - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node


    def add_to_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if not self.head:
            return False
        current = self.head
        if current.data == data:
            self.head = current.next
            return True
        while current.next and current.next.data != data:
            current = current.next
        if current.next:
            current.next = current.next.next
            return True
        return False

    def search(self, data):
        if self.head.data == data:
            return True
        current = self.head
        while current.next:
            current = current.next
            if current.data == data:
                return True
        return False
        
        

    def to_list(self):
        ls = []
        if not self.head:
            return ls
        current = self.head
        while current:
            ls.append(current.data)
            current = current.next
        return ls



if __name__ == "__main__":
    A = SinglyLinkedList()
    A.add_to(1)
    A.add_to(2)
    A.add_to(3)
    A.add_to(4)
    print(A.to_list())

