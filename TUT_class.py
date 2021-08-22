class Person:
    def __init__(self,name,age):        #constructor
        self.name=name
        self.age=age

    def talk(self):                     #self is very imp.
        print(f"Hello! My name is {name} and I am {age} years old :)")


name=input("Enter name: ")
age=input(f"Enter {name}'s age: ")
obj_person=Person(name,age)             
obj_person.talk()

name=input("Enter name: ")
age=input(f"Enter {name}'s age: ")
obj2_person=Person(name,age)
obj2_person.talk()
