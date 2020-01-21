from abc import ABC, abstractmethod

class User(ABC):
    
    def __init__(self, name, age):
        """Create a new User."""
        self.name = name
        self.age = age
        
    @abstractmethod
    def greet(self):
        pass
    

class Kate(User):
    isIndoor = True

    def __init__(self, name, age, isIndoor=True):
        """Create a new """
        self.isIndoor = isIndoor
        super().__init__(name, age)


    def greet(self):
        """Make the kate greet"""
        print(f'{self.name} says, "Hello Everyone"')
        
        
class John(User):

    def __init__(self, name:str, age:int, breed:str, weight:int):
        """Create a new John"""
        self.breed = breed
        self.weight = weight
        super().__init__(name, age)

    def greet(self) -> None:
        """Make the john greet"""
        print(f'{self.name} says, "Stay focused."')
        
class Doe(User):
    
    def __init__(self, name:str, age:int, color:str):
        """Create a new Doe"""
        self.color = color
        super().__init__(name, age)
    
    def greet(self) -> None:
        """Make Doe greet."""
        print(f'{self.name} says, "Stay Cool!!!"')
        

if __name__ == "__main__":
    doe = Doe("Doe", 6, "Red")
    katey = Kate('Katey', 3)
    johnny = John('Mr. Johnny', 4, 'Johnson..', 18)
    katey.greet()
    johnny.greet()
    doe.greet()