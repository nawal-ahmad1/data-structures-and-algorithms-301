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
            new_animal = Cat()
        elif animal == 'dog':
            new_animal = Dog()
        else:
            return "There is no new animal"

        if not self.front:
            self.front = new_animal
            self.rear = new_animal
        else:
            self.rear.next = new_animal
            self.rear = new_animal

    def dequeue(self,pref):
        pass

    def __str__(self):
        pass



