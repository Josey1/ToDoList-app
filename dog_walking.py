from pets_class import Dog

class Pet:
    """
    This time I have added another argument, Taking into consideration that for a pet to move,
    it will for sure move at a certain speed
    """
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def walk(self):
        self.speed = int(self.speed)
        return 'Since there is a speed of {}; therefore:\n {} is walking!'.format(self.speed, self.name)

dog_1 = Pet("Tom", 10)
dog_2 = Pet("Fletcher", 15)
dog_3 = Pet("Larry", 20)

print(dog_1.walk())
print(dog_2.walk())
print(dog_3.walk())



