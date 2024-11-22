from hashTable import HashTable

def test_insertItem():
    table = HashTable(10)
    table.insert('bruh', 10)
    table.insert('erm', 30)
    table.insert('spruce', 20)
    
    result = eval(str(table))  # Convert the string back to a list of tuples
    expected = [('spruce', 20), ('erm', 30), ('bruh', 10)]
    
    assert set(result) == set(expected)  # Compare as sets to ignore order

def test_removeLastItem():
    table = HashTable(10)
    table.insert('bruh', 10)
    table.insert('erm', 30)
    table.insert('spruce', 20)
    table.remove('spruce')

    result = eval(str(table))  # Convert the string back to a list of tuples
    expected = [('erm', 30), ('bruh', 10)]
    
    assert set(result) == set(expected)  # Compare as sets to ignore order

def test_searches():
    table = HashTable(10)
    table.insert('bruh', 10)
    table.insert('erm', 30)
    table.insert('spruce', 20)
    
    assert table.search('spruce') == 20
    


"""
class Node:
    def __init__(self, key, value) -> None:

class HashTable:
    def __init__(self, capacity) -> None:
    def _hash(self, key):
    def insert(self, key, value):
    def __str__(self) -> str:
    def search(self, key):
    def remove(self, key):
    def len(self):
    def __contains__(self, key):
        
 if __name__ == "__main__":
     table = HashTable(10)
     table.insert('bruh', 10)
    table.insert('erm', 30)
     table.insert('spruce', 20)
    print(str(table))
"""