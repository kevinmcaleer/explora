from animals import Animal

class Mammal(Animal):

    def __init__(self, name = None):
        super().__init__(name)

    @property
    def legs(self):
        return 4

    @property
    def blood_type(self):
        return "Warm"

    @property
    def birth_type(self):
        return "Live"

    @property
    def zoo_class(self):
        return "Mammal"

    def show(self):
        super().show()
        