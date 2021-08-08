# Stacks and Queues

## Code Challenge: Stacks and Queues
A stack is a data structure that consists of Nodes depends on --> last in last out.

## Challenge
Create stack class with push, pop, peek and is empty methods. 
Create queue class with enqueue, dequeue, peek and is empty methods.

## Approach & Efficiency

**For Stacks**
- push : O(1)
- pop : O(1)
- peek : O(1)
- is_empty : O(1)

**For Queues**
- enqueue : O(1)
- dequeue : O(1)
- peek : O(1)
- is_empty : O(1)

## API

### Stacks
**push**: add to a stack new values.
**pop**: delete from the stack.
**peek**: view the value of the top Node in the stack.
**is_empty**: returns true when stack is empty.

### Queues
**enqueue**: add to the queue.
**dequeue**: remove from the queue.
**peek**: view the value of the front Node in the queue.
**is_empty** returns true when queue is empty.

### Queues Pseudo 
Create PseudoQueue class depends on first in first out for stack methods.
**enqueue**: add to the stack.
**dequeue**: remove first in element from the stack. 

**For Queues Pseudo Approach**
- enqueue : O(1)
- dequeue : O(1)
