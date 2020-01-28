from .user import User

class Kate(User):
    isIndoor = True

    def __init__(self, name, age, isIndoor=True):
        """Create a new """
        self.isIndoor = isIndoor
        super().__init__(name, age)


    def greet(self):
        """Make the kate greet"""
        print(f'{self.name} says, "Hello Everyone"')
   