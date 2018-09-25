class Pet:
    """
    Creating a Pets class and defining a special init method 
    with an instance self and two others arguments; name and age 
    of the dogs and setting all the instance variables
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age
    """defining a function to enable me output the details of 
    the attributes of my three dogs
    """
    def dog_details(self):
        return '{} is {}'.format(self.name, self.age)

    """
    Creating my three instances of the class Pets; so that the 
    instance is passed automatically
    """
dog_1 = Pet("Tom", 6)
dog_2 = Pet("Fletcher", 7)
dog_3 = Pet("Larry", 9)



class Dog:
    """
    Creating another class; Dog with an instance variable
    is_hungry
    """
    def __init__(self, is_hungry):
        is_hungry = True
        print("My dogs are hungry")
    """
    defining another method; eat() which changes the value of 
    is_hungry to False.
    """
    def eat(self):
        is_hungry = False
        print("My dogs are not hungry")
    """
    determing whether my dogs are hungry or not by defining a
    function for their behaviour
    """
    def behavior(self, mood):
        print ("Dog is happy")

print("I have three dogs")
print(dog_1.dog_details())
print(dog_2.dog_details())
print(dog_3.dog_details())
print("And they're all mammals, ofcourse.")
print("My dogs are not hungry")
        






    
    