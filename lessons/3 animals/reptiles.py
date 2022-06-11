from animals import Animal
from abc import abstractproperty

class Reptile(Animal):
    
    @abstractproperty
    def legs(self):
        pass

    @property
    def birth_type(self):
        return 'Egg'

    @property
    def blood_type(self):
        return 'Cold'
    
    @property
    def zoo_class(self):
        return "Reptile"