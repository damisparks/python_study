from .user import User 
        
class Doe(User):
    
    def __init__(self, name:str, age:int, color:str):
        """Create a new Doe"""
        self.color = color
        super().__init__(name, age)
    
    def greet(self) -> None:
        """Make Doe greet."""
        print(f'{self.name} says, "Stay Cool!!!"')
      