from stack_and_queue.stack_and_queue import *

# import pytest

# test push onto a stack
def test_push():
    stack = Stack()
    stack.push(27)
    actual = stack.top.value
    assert actual == 27

#test push multiple values onto a stack
def test_push_multiple():
    stack = Stack()
    stack.push(3)
    stack.push(2)
    stack.push(1)
    actual = stack.top.value
    assert actual == 1

#test pop off the stack
def test_pop():
    stack = Stack()
    stack.push(3)
    stack.push(2)
    stack.push(1)
    actual = stack.pop()
    assert actual == 1

#test empty a stack after multiple pops
def test_pop_multiple():
    stack = Stack()
    stack.push(3)
    stack.push(2)
    stack.push(1)
    stack.pop() #1
    actual = stack.pop() #2
    assert actual == 2

#test peek the next item on the stack
def test_peek():
    stack = Stack()
    stack.push(3)
    stack.push(6)
    stack.push(9)
    actual = stack.peek()
    assert actual == 9

#test instantiate an empty stack
def test_is_empty():
    stack = Stack()
    actual = stack.top
    assert actual == None

#Calling pop or peek on empty stack raises exception
def test_raises_exception():
    stack = Stack()
    actual = stack.peek()
    assert actual == "Stack is empty"

#test enqueue into a queue
def test_enqueue():
    queue = Queue()
    queue.enqueue(9)
    actual = queue.front.value
    assert actual == 9

#test enqueue multiple values into a queue
def test_enqueue_multiple():
    queue = Queue()
    queue.enqueue(9)
    queue.enqueue(3)
    actual = queue.front.next.value
    assert actual == 3

#test dequeue out of a queue the expected value
def test_dequeue():
    queue = Queue()
    queue.enqueue(9)
    queue.enqueue(3)
    queue.dequeue()
    actual = queue.front.value  
    assert actual == 3

#test peek into a queue, seeing the expected value
def test_peek_queue():
    queue = Queue()
    queue.enqueue(9)
    queue.enqueue(3)
    queue.enqueue(1)
    actual = queue.peek()
    assert actual == 9

#test empty a queue after multiple dequeues
def test_empty_queue():
    queue = Queue()
    queue.enqueue(5)
    queue.enqueue(10)
    queue.dequeue()
    queue.dequeue()
    actual = queue.front
    assert actual == None

#test instantiate an empty queue
def test_instantiate_queue():
    queue = Queue()
    actual = queue.front
    assert actual == None

#test dequeue or peek on empty queue raises exception
def test_exception_queue():
    queue = Queue()
    actual = queue.peek()
    assert actual == "Queue is empty"


# Stack enqueue 
def test_pseudo_enqueue():
    psq = PseudoQueue()
    psq.enqueue(10)
    actual = psq.stack1.top.value
    assert actual == 10

# Stack enqueue multiple
def test_pseudo_enqueue_multiple():
    psq = PseudoQueue()
    psq.enqueue(10)
    psq.enqueue(20)
    actual = psq.stack1.top.value
    assert actual == 20

# Stack dequeue 
def test_pseudo_dequeue():
    psq = PseudoQueue()
    psq.enqueue(10)
    actual = psq.dequeue()
    assert actual == 10

# Stack dequeue multiple
def test_pseudo_dequeue_multiple():
    psq = PseudoQueue()
    psq.enqueue(10)
    psq.enqueue(20)
    psq.enqueue(30)
    actual = psq.dequeue()
    assert actual == 10

#raises exception
def test_pseudo_exception():
    psq = PseudoQueue()
    actual = psq.dequeue()
    assert actual == "Stack is empty"
