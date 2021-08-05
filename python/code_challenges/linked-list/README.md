# Singly Linked List

## Challenge

Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node, LinkedList class include a head property.

## Approach & Efficiency

Singly Linked List.
O(1) Time/space performance for insert method.
O(n) Time and O(1) space performance for includes method.
O(n) Time and O(1) space performance for insert_before method.
O(n) Time and O(1) space performance for insert_after method.
O(n) Time and O(n) space performance for kth method.

## Methods

**insert method**
Takes a value as an argument and add new node to the head hold that value.

**includes method**
Takes a value as an argument and returns a boolean.

**append method**
Takes a value as an argument and adds a new node to the end hold that.
![append](python/code_challenges/linked-list/assets/append.jpg)

**insertBefore method**
Add a new node with the given new value before the first node.
![insert_before](python/code_challenges/linked-list/assets/insert-before.jpg)

**insertAfter method**
Add a new node with the given new value after the first node.
![insert_after](python/code_challenges/linked-list/assets/insert-after.jpg)

**kthFromEnd**
Takes a number (k) as a parameter and return the node’s value that is k from the end of the linked list.
![kth](python/code_challenges/linked-list/assets/kth.jpg)