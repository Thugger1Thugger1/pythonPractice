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

    def _hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        index = self._hash(key)
        if self.table[index] is None: 
            self.table[index] = Node(key, value) 
            self.size += 1
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            newNode = Node(key, value)
            newNode.next = self.table[index]
            self.table[index] = newNode
            self.size += 1


    def __str__(self) -> str:
        ret = []
        for i in range(self.capacity):
            current = self.table[i]

            while current:
                ret.append((current.key, current.value))
                current = current.next
        return str(ret)
    
    def search(self, key):
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return "not in table"

    def remove(self, key):
        index = self._hash(key)
        current = self.table[index]
        if not current:
            return False

        if not current.next and current.key == key:
            self.table[index] = None
            self.size -= 1
            return True
        while current.next:
            if current.next.key == key:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next
        return False

    def len(self):
        return self.size

    def __contains__(self, key):
        try:
            self.search(key)
            return True
        except KeyError:
            return False




if __name__ == "__main__":
    table = HashTable(10)
    table.insert('bruh', 10)
    table.insert('erm', 30)
    table.insert('spruce', 20)
    print(str(table))