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

insert method
Takes a value as an argument and add new node to the head hold that value.

includes method
Takes a value as an argument and returns a boolean.

append method
Takes a value as an argument and adds a new node to the end hold that.

insertBefore method
Add a new node with the given new value before the first node

insertAfter method
Add a new node with the given new value after the first node

kthFromEnd
Takes a number (k) as a parameter and return the node’s value that is k from the end of the linked list.

str method
returns a string with Linked List values: a -> b -> c -> NULL.