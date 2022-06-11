from mammals import Mammal


class Dog(Mammal):
    _breed = ""
    _weight = 20
    
    def __init__(self, name=None, breed=None):
        super().__init__(name)
        if breed is not None:
            self._breed = breed
        if name:
            self.name = name

    def wag(self):
        """ Wag the tail """
        print('wags tail')

    @property
    def breed(self):
        """ Return the Dogs breed """
        return self._breed

    @breed.setter
    def breed(self, value):
        """ Set the Dogs breed """
        self._breed = value

    @property
    def weight(self):
        """ Get the Dogs weight """
        return self._weight

    def show(self):
        super().show()
        print(f"Breed: {self.breed}")