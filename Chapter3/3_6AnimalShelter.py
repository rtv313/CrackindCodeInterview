
class Dog:
    def __init__(self,arrival_order_general):
        self.type = 'Dog'
        self.arrival_order_general = arrival_order_general


class Cat:
    def __init__(self,arrival_order_general):
        self.type = 'Cat'
        self.arrival_order_general = arrival_order_general


class Shelter:
    # enqueue, dequeueAny, dequeueDog, and dequeueCat
    def __init__(self):
        self.counter = 0
        self.dogs = list()
        self.cats = list()
        pass

    def enqueue(self,type):

        if type == 'Dog':

            if len(self.dogs) == 0:
                new_dog = Dog(self.counter)
                self.dogs.append(new_dog)
            else:
                new_dog = Dog(self.counter)
                self.dogs.append(new_dog)

        if type == 'Cat':

            if len(self.cats) == 0:
                new_cat = Cat(self.counter)
                self.cats.append(new_cat)
            else:
                new_cat = Cat(self.counter)
                self.cats.append(new_cat)

        self.counter += 1

    def dequeue_dog(self):
        if len(self.dogs) != 0:
            return self.dogs.pop(0)
        return None

    def dequeue_cat(self):
        if len(self.cats) != 0:
            return self.cats.pop(0)
        return None

    def dequeue_any(self):

        if len(self.dogs) == 0 and len(self.cats) == 0:
            return None

        if len(self.dogs) == 0:
            return self.dequeue_cat()

        if len(self.cats) == 0:
            return self.dequeue_dog()

        dog = self.dogs[0]
        cat = self.cats[0]

        if dog.arrival_order_general < cat.arrival_order_general:
            return self.dogs.pop(0)
        else:
            return self.cats.pop(0)


shelter = Shelter()

shelter.enqueue('Dog')
shelter.enqueue('Dog')
shelter.enqueue('Dog')

shelter.enqueue('Cat')
shelter.enqueue('Cat')
shelter.enqueue('Cat')

shelter.enqueue('Dog')


print(shelter.dequeue_any().type)
print(shelter.dequeue_any().type)
print(shelter.dequeue_any().type)
print(shelter.dequeue_any().type)

print(shelter.dequeue_dog().type)
print(shelter.dequeue_cat().type)

print(shelter.dequeue_any().type)