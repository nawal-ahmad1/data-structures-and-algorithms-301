from typing import Counter
from stack_and_queue import Stack

class PseudoQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value): #Insert - first in first out approach
        self.stack1.push(value)

    def __str__(self):
        return str(self.stack1)
    
    def dequeue(self): #Extract - first in first out approach
        current = self.stack1.top
        while current:
            self.stack2.push(current.value)
            current = current.next
            self.stack1.pop()
            if current == None:
                break
        output = self.stack2.pop()
        current = self.stack2.top
        while current:
            self.stack1.push(current.value)
            current = current.next
            self.stack2.pop()
            if current == None:
                break
        return output


if __name__ == "__main__":
    pq = PseudoQueue()
    pq.enqueue(20)
    pq.enqueue(15)
    pq.enqueue(10)
    pq.enqueue(5)
    pq.dequeue()
    pq.dequeue()
    print(str(pq))


