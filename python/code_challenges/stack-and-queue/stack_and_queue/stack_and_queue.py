class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class StackEmptyException(Exception):
	pass

class Stack:
    def __init__(self):
        self.top = None

    def push(self,value):
        node = Node(value)
        if self.top:
            node.next = self.top
            self.top = node   
        else: 
            self.top = node

    def pop(self):
        if not self.top:
            return "Stack is empty"
            # raise Exception("Stack is empty") 
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp.value

    def peek(self):
        if not self.top:
            return "Stack is empty"
            # raise Exception("Stack is empty") 
        else: 
            return self.top.value

    def is_empty(self):
        if self.top:
            return False
        return True


class Queue():
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,value):
        node = Node(value)
        if not self.front:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = self.rear.next

    def dequeue(self):
        if not self.front:
            return "Queue is empty"
            # raise Exception("Queue is empty")
        else: 
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp.value

    def peek(self):
        if not self.is_empty():
            return self.front.value
        else:
            return "Queue is empty"
            # raise Exception("Queue is empty")

    def is_empty(self):
        if self.front:
            return False
        return True
