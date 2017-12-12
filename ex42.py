## Animal is-a object
class Animal(object):
    pass

## dog is-a animal
class Dog(Animal):

    def __init__(self, name):
        ## the dog has-a name
        self.name = name

 ## cat is-a animal
class Cat(Animal):

    def __init__(self, name):
        ## the cat has-a name
        self.name = name

## person is-a object
class Person(object):

    def __init__(self, name):
        ## person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## employee is-a person
class Employee(Person):

    def __init__(self, name, salary):
        ## employee has-a name
        super(Employee, self).__init__(name)
        ## employee has-a salary
        self.salary = salary

## fish is-a object
class Fish(object):
    pass

## salmon is-a fish
class Salmon(Fish):
    pass

## halibut is-a fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Satan")

## mary is-a person's name
mary = Person("Mary")

## mary's pet is-a satan
mary.pet = satan

## employee Frank has-a salary of 120000
frank = Employee("Frank", 120000)

## frank's pet is-a rover
frank.pet = rover

## flipper is-a fish
flipper = Fish()

## crouse is-a salmon
crouse = Salmon()

## harry is-a halibut
harry = Halibut()
