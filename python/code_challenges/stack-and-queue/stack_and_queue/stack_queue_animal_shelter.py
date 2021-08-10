class Cat():
    def __init__(self,value = 'cat'):
        self.value=value
        self.next= None

    def __str__(self):
        return f"{self.value}"



class Dog():
    def __init__(self,value = 'dog'):
        self.value=value
        self.next= None

    def __str__(self):
        return f"{self.value}"


class  AnimalShelter:
    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue(self,animal):
        if animal == 'cat':
            animal = Cat()
        elif animal == 'dog':
            animal = Dog()
        else:
            animal = None

        if not self.front:
            self.front = animal
            self.rear = animal
        else:
            self.rear.next = animal
            self.rear = animal

    def dequeue(self,pref):
        if pref =='cat' or pref =='dog':
            current = self.front
            self.front = current.next
            current.next = None    
            return current     
        else:
            return 'null'


    def __str__(self):
        if self.front:
            string = ""
            current = self.front
            while current != None:
                string += str(current.value) + ' '
                current = current.next
            return string

if __name__ == "__main__":
    sq = AnimalShelter()
    sq.enqueue('cat')
    sq.enqueue('dog')
    sq.enqueue('dog')
    sq.enqueue('cat')
    sq.enqueue('dog')
    print(sq.front)

    # sq.dequeue('dog')
    # sq.dequeue('dog')
    print((sq))






