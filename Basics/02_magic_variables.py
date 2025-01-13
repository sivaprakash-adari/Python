from dataclasses import dataclass
from abc import ABC,abstractmethod

print("Starting the 02_magic_variables program")

def function1():
    print("Inside function one")

def function2():
    print("Inside function two")

@dataclass
class Animal:
    name:str
    color:str
    age:int

    def __str__(self):
        return f"{self.name} in {self.color} color"

    @abstractmethod
    def speak():
        pass

class Domestic(Animal):
    def __init__(self,name,color,age):
        super().__init__(name,color,age)

    def speak(self):
        match self.name:
            case "Cat" : print("meow")
            case "Dog" : print("bow")
            case "-"   : print("no one speaks")


if __name__ == "__main__":
    function1()
    function2()

    A1 = Domestic("Cat", "Black",2)
    A2 = Domestic("Rabbit", "White", 3)

    print(A1)
    print(A2)
    print(A1.__dict__)

    A1.speak()
    A2.speak()