from hashTable import HashTable

def test_insertItem():
    hashtable = HashTable(10)
    hashtable.insert('bruh', 1)
    
    assert print(hashtable) == "('bruh', 1)"