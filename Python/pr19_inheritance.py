# Inheritance : It is used to form a new class from the classes that are already defined. The newly formed class are called Derived class or a child class and from which the new class are derived is known as base class/parent class.The derived class override or extends the methods/function of the parent class.

class Animal:
    def __init__(self):
        print('Animal class Created')
    def who(self):
        print("Animal")

    def eat(self):
        print("It is omnivorous")

class Dog(Animal):
    def who(self):
        print('Dog')

    def speak(self):
        print('Bark')

class Husky(Dog):
    def who(self):
        print("Husky")

obj_a=Animal()
print(obj_a)
obj_a.who()
obj_a.eat()

obj_b=Dog()
obj_b.who()
obj_b.speak()

obj_c=Husky()
obj_c.who()
obj_c.eat()
obj_c.speak()
