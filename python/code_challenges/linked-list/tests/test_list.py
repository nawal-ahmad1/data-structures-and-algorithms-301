import pytest

from linked_list.linked_list import LinkedList, Node

# 1
# instantiate an empty linked list


def test_insert():
    ll = LinkedList()
    with pytest.raises(AttributeError):
        ll.head.value
    ll.insert(None)
    actual = ll.head.value
    assert actual == None

# 2
#  insert into the linked list


def test_insert():
    ll = LinkedList()
    with pytest.raises(AttributeError):
        ll.head.value
    ll.insert(5)
    actual = ll.head.value
    assert actual == 5

# 3
# point to the first node in the linked list


def test_first_node():
    node = Node("Hello")
    actual = node.value
    assert actual == "Hello"

# 4
# multiple nodes into the linked list


def test_multiple_node():
    node = Node("World")
    actual = node.next
    assert True

# 5
# return a collection of all the values that exist in the linked list


def test_collection():
    ll = LinkedList()
    with pytest.raises(AttributeError):
        ll.head.value
    ll.insert(7)
    actual = ll.head.value
    assert actual == 7
