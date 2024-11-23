from doublyLinkedList import DoublyLinkedList


def test_addToBack():
    ll = DoublyLinkedList()
    ll.addToBack(1)
    ll.addToBack(2)
    ll.addToBack(3)
    ll.addToBack(4)

    assert ll.toList() == [1, 2, 3, 4]

def test_addToFront():
    ll = DoublyLinkedList()
    ll.addToFront(1)
    ll.addToFront(2)
    ll.addToFront(3)
    ll.addToFront(4)

    assert ll.toList() == [4, 3, 2, 1]

def test_append_to_index():
    ll = DoublyLinkedList()
    ll.addToBack(1)
    ll.addToBack(2)
    ll.addToBack(3)
    ll.addToBack(4)
    ll.addToIndex(6, 2)

    assert ll.toList() == [1, 2, 6, 3, 4]

def test_delete_existing():
    ll = DoublyLinkedList()
    ll.addToBack(1)
    ll.addToBack(2)
    ll.addToBack(3)
    assert ll.delete(2) is True
    assert ll.toList() == [1, 3]

def test_delete_non_existing():
    ll = DoublyLinkedList()
    ll.addToBack(1)
    ll.addToBack(2)
    ll.addToBack(3)
    assert ll.delete(99) is False
    assert ll.toList() == [1, 2, 3]

def test_delete_head():
    ll = DoublyLinkedList()
    ll.addToBack(1)
    ll.addToBack(2)
    ll.addToBack(3)
    assert ll.delete(1) is True
    assert ll.toList() == [2, 3]

def test_delete_tail():
    ll = DoublyLinkedList()
    ll.addToBack(1)
    ll.addToBack(2)
    ll.addToBack(3)
    assert ll.delete(3) is True
    assert ll.toList() == [1, 2]

def test_search_existing():
    ll = DoublyLinkedList()
    ll.addToBack(1)
    ll.addToBack(2)
    ll.addToBack(3)
    assert ll.search(2) is True

def test_search_non_existing():
    ll = DoublyLinkedList()
    ll.addToBack(1)
    ll.addToBack(2)
    ll.addToBack(3)
    assert ll.search(99) is False

def test_to_list_empty():
    ll = DoublyLinkedList()
    ll.addToBack(1)
    ll.addToBack(2)
    ll.addToBack(3)
    ll = DoublyLinkedList()
    assert ll.toList() == []

def test_to_list():
    ll = DoublyLinkedList()
    ll.addToBack(1)
    ll.addToBack(2)
    ll.addToBack(3)
    assert ll.toList() == [1, 2, 3]