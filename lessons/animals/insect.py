from abc import abstractproperty
from animals import Animal

class Insect(Animal):
    
    def __init__(self, name) -> None:
        super().__init__(name)

    @abstractproperty
    def can_fly(self):
        pass

    @property
    def legs(self):
        return 6

    @property
    def birth_type(self):
        return "Egg"

    @property
    def blood_type(self):
        return "Cold"

    @property
    def zoo_class(self):
        return "Insect"