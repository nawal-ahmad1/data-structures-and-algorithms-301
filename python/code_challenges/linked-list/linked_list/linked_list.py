class Node():
    def __init__(self, value=""):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

    def __add__(self, other):
        return Node(self.value + other.value)

class LinkedList():
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)
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

    def append(self,value):
        node=Node(value)
        current=self.head
        if current==None:
            self.insert(value)
            return
        while current.next!=None:
            current=current.next
        current.next=node
    # def insert_before(self,flag,before):
    #     head = self.head
    #     next_value = self.head
    #     node = Node(before)
    #     if str(flag) == str(self.head):
    #         self.insert(before)
    #         return
    #     while flag != next_value.value:
    #         head = next_value
    #         next_value = next_value.next
    #     head.next = node
    #     node.next = next_value

    # def insert_after(self,previous,value):
    #     node = Node(value)
    #     current = self.head
    #     temp = self.head
    #     while current.next!= None:
    #         if current.value == previous:
    #             temp = temp.next
    #             current.next = node
    #             current = current.next
    #             current.next = temp
    #             return
    #         current = current.next
    #         temp = temp.next
    #         self.append(value)

    def __str__(self):
        string = ""
        current = self.head
        while current:
            string += f"{str(current.value)} -> "
            current = current.next
        string += "None"
        return string

    def __iter__(self):
        # new_list = []
        current = self.head

        while current:
            yield current.value
            current = current.next
        # return new_list

    def __repr__(self):
        return "LinkedList()"

    # def kthFromEnd(self,k):
    #     last_node = len(self)-1

    #     if last_node < k:
    #         return ("Exception!")
    #     steps = (len(self)-k)-1
    #     current = self.head

    #     while steps > 0 :
    #         current = current.next
    #         steps -= 1
    #     return current.value

def zipLists(list1,list2):
    current1 = list1.head
    current2 = list2.head
    if current1 == None or current2 == None:
        if current1:
            return list1.__str
        elif current2:
            return list2.__str__
        else:
            return "Both Lists are empty"
                
    zip_list=[]
    while current1 or current2:
        if current1:
            zip_list += [current1.value]
            current1 = current1.next
        if current2:
            zip_list += [current2.value]
            current2 = current2.next
    output=''
    for i in zip_list:
        output+=f'{i}-> '
    output+='None'
    return output



if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(7)
    ll.insert(9)
    ll.insert(11)
    ll.insert(18)

    print(ll)
    node1 = Node(1)
    node2 = Node(2)
    print(node1)
    for value in ll:
        print(value)

    # ll.insert_before(18,55)
    # ll.insert_after(11,7)

    list1=LinkedList()
    list2=LinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(5)
    list2.append(2)
    list2.append(4)
    list2.append(6)
    print(list1.__str__())
    print(list2.__str__())
    print(zipLists(list1,list2).__str__())
