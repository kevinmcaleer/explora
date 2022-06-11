# Mammal class
# Kevin McAleer
# June 2022

from mammals import Mammal

class Cat(Mammal):
    _breed = ""

    def __init__(self, name=None, breed=None):
        super().__init__(name)
        if breed is not None:
            self._breed = breed
        if name:
            self.name = name

    @property
    def breed(self):
        """ Return the breed of cat """
        return self._breed

    @breed.setter
    def breed(self, value):
        """ Set the breed of cat """
        self._breed = value

    def show(self):
        super().show()
        print(f"breed: {self.breed}")