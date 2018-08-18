## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal object
class Dog(Animal):
    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat is-a Animal object
class Cat(Animal):
    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self,name):
        ## Person has-a name
        self.name = name
        ## Person has a pet
        self.pet = None

## Employee is a Person object
class Employee(Person):

    def __init__(self, name, salary):
        ## Employee has-a name (property from Person)
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish object
class Salmon(Fish):
    pass

## Halibut is-a Fish object
class Halibut(Fish):
    pass

## rover is-a Dog object
rover = Dog("Rover")

## satan is-a Cat object
satan = Cat("Satan")

## mary is-a Person object
mary = Person("Mary")

# mary has-a pet property. satan is-a Pet object
mary.pet = satan

## frank has-a salary property. frank is-a Employee object
frank = Employee("Frank", 120000)

## frank has-a pet property. rover is-a pet object
frank.pet = rover

#flipper is-a Fish object
flipper = Fish()

#crouse is-a Salmon object
crouse = Salmon()

# harry is-a Halibut object
harry = Halibut()
