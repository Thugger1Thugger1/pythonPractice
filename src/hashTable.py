class Node:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.next = None
        
class HashTable:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    
    def _hash(self, key) -> None:
        return hash(key) % self.capacity

    def insert(self, key, value) -> None:
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                current.value = value
                return
            current = current.next
        NewNode = Node(key, value)
        NewNode.next = self.table[index]
        self.table[index] = NewNode
        self.size =+ 1

    def __str__(self) -> str:
        ret = []
        for i in range(len(self.table)):
            current = self.table[i]
            while current:
                ret.append((current.key, current.value))
                current = current.next
        return str(ret)

    def remove(self, key) -> bool:
        index = self._hash(key)
        if not self.table[index]:
            return False
        current = self.table[index]
        if not current.next and current.key == key:
            self.table[index] = None
        while current.next:
            if current.next.key == key:
                current.next = current.next.next
                size -= 1
                return True
            current = current.next
        return False

    def search(self, key):
        index = self._hash(key)
        if not self.table[index]:
            return False
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return False 

    def toList(self) -> str:
        ret = []
        for i in range(len(self.table)):
            current = self.table[i]
            while current:
                ret.append((current.key, current.value))
                current = current.next
        return ret

             


if __name__ == "__main__":
    table = HashTable(10)
    table.insert('bruh', 10)
    table.insert('erm', 30)
    table.insert('spruce', 20)
    print(table.remove('asdf'))
    print(table)
