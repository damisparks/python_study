from .user import User

class John(User):

    def __init__(self, name:str, age:int, breed:str, weight:int):
        """Create a new John"""
        self.breed = breed
        self.weight = weight
        super().__init__(name, age)

    def greet(self) -> None:
        """Make the john greet"""
        print(f'{self.name} says, "Stay focused."')
    