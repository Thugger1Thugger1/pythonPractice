from singlyLinkedList import SinglyLinkedList


def test_append():
    ll = SinglyLinkedList()
    ll.add_to(1)
    ll.add_to(2)
    ll.add_to(3)
    ll.add_to(4)

    assert ll.to_list() == [1, 2, 3, 4]

def test_append_to_start():
    ll = SinglyLinkedList()
    ll.add_to_start(1)
    ll.add_to_start(2)
    ll.add_to_start(3)
    ll.add_to_start(4)

    assert ll.to_list() == [4, 3, 2, 1]

def test_append_to_index():
    ll = SinglyLinkedList()
    ll.add_to_start(1)
    ll.add_to_start(2)
    ll.add_to_start(3)
    ll.add_to_start(4)
    ll.append_to_index(6, 2)

    assert ll.to_list() == [4, 3, 6, 2, 1]

def test_delete_existing():
    ll = SinglyLinkedList()
    ll.add_to(1)
    ll.add_to(2)
    ll.add_to(3)
    assert ll.delete(2) is True
    assert ll.to_list() == [1, 3]

def test_delete_non_existing():
    ll = SinglyLinkedList()
    ll.add_to(1)
    ll.add_to(2)
    ll.add_to(3)
    assert ll.delete(99) is False
    assert ll.to_list() == [1, 2, 3]

def test_delete_head():
    ll = SinglyLinkedList()
    ll.add_to(1)
    ll.add_to(2)
    ll.add_to(3)
    assert ll.delete(1) is True
    assert ll.to_list() == [2, 3]

def test_delete_tail():
    ll = SinglyLinkedList()
    ll.add_to(1)
    ll.add_to(2)
    ll.add_to(3)
    assert ll.delete(3) is True
    assert ll.to_list() == [1, 2]

def test_search_existing():
    ll = SinglyLinkedList()
    ll.add_to(1)
    ll.add_to(2)
    ll.add_to(3)
    assert ll.search(2) is True

def test_search_non_existing():
    ll = SinglyLinkedList()
    ll.add_to(1)
    ll.add_to(2)
    ll.add_to(3)
    assert ll.search(99) is False

def test_to_list_empty():
    ll = SinglyLinkedList()
    ll.add_to(1)
    ll.add_to(2)
    ll.add_to(3)
    ll = SinglyLinkedList()
    assert ll.to_list() == []

def test_to_list():
    ll = SinglyLinkedList()
    ll.add_to(1)
    ll.add_to(2)
    ll.add_to(3)
    assert ll.to_list() == [1, 2, 3]
