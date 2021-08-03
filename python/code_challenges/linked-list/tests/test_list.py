import pytest

from linked_list.linked_list import LinkedList, Node

# 1
# instantiate an empty linked list

def test_empty_linked_list():
    ll=LinkedList()
    actual = list(ll)
    expected = []
    assert actual == expected


# 2
#  insert into the linked list

def test_inser():
    ll = LinkedList()
    with pytest.raises(AttributeError):
        ll.head.value
    ll.insert(11)
    actual = ll.head.value
    assert actual==11

# 3
# point to the first node in the linked list

def test_first_node():
    node = Node('Hello')
    actual= node.value
    assert actual == 'Hello'

# 4
# multiple nodes into the linked list


def test_multiple_node():
  node = Node("World")
  actual = node.next
  assert True



# 5
# return true when finding a value within the linked list that exists

def test_exist():
    ll = LinkedList()
    ll.insert(7)
    ll.insert(6)
    ll.insert(5)
    ll.insert(4)
    actual=ll.includes(4)
    assert actual == True

#6
# return false when searching for a value in the linked list that does not exist
def test_non_exist():
    ll = LinkedList()
    with pytest.raises(AttributeError):
        ll.head.value
    ll.insert(11)
    actual = ll.includes(23)
    assert actual == False

#7
# return a collection of all the values that exist in the linked list
def test_collection():
    ll=LinkedList()
    ll.insert(45)
    actual = ll.includes(45)
    expected = True
    assert actual == expected


#8
#  add a node to the end of the linked list
def test_add_end():
    ll= LinkedList()
    ll.insert(7)
    ll.append(27)
    assert ll.includes(27)

#9
# add multiple nodes to the end of a linked list
def test_add_multiple():
    ll= LinkedList()
    ll.insert(7)
    ll.append(27)
    ll.append(37)
    ll.append(40)
    assert ll.includes(27)

#10
# insert a node before a node located in the middle of a linked list
def test_add_to_middle():
    ll= LinkedList()
    ll.insert(7)
    ll.insert(27)
    ll.insert(35)
    ll.insert(40)
    ll.insert_before(35,15)
    assert ll.includes(15)

#11
#insert a node before the first node of a linked list
def test_add_befor_first():
    ll= LinkedList()
    ll.insert(4)
    ll.insert(11)
    ll.insert(25)
    ll.insert(40)
    ll.insert_before(40,35)
    assert ll.includes(35)

#12
# insert after a node in the middle of the linked list
def test_add_after_middle():
    ll= LinkedList()
    ll.insert(4)
    ll.insert(11)
    ll.insert(25)
    ll.insert(40)
    ll.insert_after(25,35)
    assert ll.includes(35)

#13
# insert a node after the last node of the linked list
def test_add_after_lasr():
    ll= LinkedList()
    ll.insert(4)
    ll.insert(11)
    ll.insert(25)
    ll.insert(40)
    ll.insert_after(40,50)
    assert ll.includes(50)
