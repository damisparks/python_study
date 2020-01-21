from abc import ABC, abstractmethod

class Animal(ABC):
    
    def __init__(self, name, age):
        """Create a new animal."""
        self.name = name
        self.age = age
        
    @abstractmethod
    def speak(self):
        pass
    

class Cat(Animal):
    isIndoor = True

    def __init__(self, name, age, isIndoor=True):
        """Create a new cat"""
        self.isIndoor = isIndoor
        super().__init__(name, age)


    def speak(self):
        """Make the cat pur"""
        print(f'{self.name} says, "purrrrrr"')
        
        
class Dog(Animal):

    def __init__(self, name:str, age:int, breed:str, weight:int):
        """Create a new dog"""
        self.breed = breed
        self.weight = weight
        super().__init__(name, age)

    def speak(self) -> None:
        """Make the dog bark"""
        print(f'{self.name} says, "woof"')
        
class Frog(Animal):
    
    def __init__(self, name:str, age:int, color:str):
        """Create a new frog"""
        self.color = color
        super().__init__(name, age)
    
    def speak(self) -> None:
        """Make frog speak."""
        print(f'{self.name} says, "croak!!!"')
        

if __name__ == "__main__":
    frogy = Frog("Froggy", 6, "Red")
    wiskers = Cat('Wiskers', 3)
    paws = Dog('Mr. Paws', 4, 'dachshund', 18)
    wiskers.speak()
    paws.speak()
    frogy.speak()