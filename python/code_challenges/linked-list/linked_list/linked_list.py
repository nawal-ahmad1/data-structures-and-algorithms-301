class Node():
    def __init__(self, value=""):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList():
    def __init__(self):
        self.head = None

    def insert(self, value):
        node = Node(value)
        if self.head:
            node.next = self.head
        self.head = node

    def includes(self, data):
        boolean = False
        current = self.head
        while current:
            if current.value == data:
                boolean = True
                break
            current = current.next
        return boolean

    def __str__(self):
        string = ""
        current = self.head
        while current:
            string += f"{str(current.value)} -> "
            current = current.next
        string += "None"
        return string

    def __iter__(self):
        new_list = []
        current = self.head

        while current:
            yield current.value
            current = current.next
        return new_list

    def __repr__(self):
        return "LinkedList()"


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(7)
    ll.insert(9)
    ll.insert(11)
    print(ll)
    node1 = Node(1)
    node2 = Node(2)
    for value in ll:
        print(value)
