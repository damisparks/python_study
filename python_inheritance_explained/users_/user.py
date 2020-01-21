from abc import ABC, abstractmethod

class User(ABC):
    
    def __init__(self, name, age):
        """Create a new User."""
        self.name = name
        self.age = age
        
    @abstractmethod
    def greet(self):
        pass