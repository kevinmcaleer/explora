# Top of the animal hierarchy
# Kevin McAleer
# June 2022

# Import abstractproperty and ABC from the Abstract Base Class library
from abc import abstractproperty, ABC

class Animal(ABC):
    """ Define the Animal Class to be inherited by other classes """

    # define a name for all animals to have 
    __name = ""

    @property
    def name(self):
        """ get the Animal name """
        return self.__name
    
    @name.setter
    def name(self, value):
        """ Set the Animal name """
        self.__name = value

    @abstractproperty
    def legs(self):
        """ Retun the number of legs the Animal has """
        pass

    @abstractproperty
    def birth_type(self):
        """ Return the type of birth the Animal has, e.g. Live or from an Egg"""
        pass

    @abstractproperty
    def blood_type(self):
        """ Return if the animal is hot or cold blooded """
        pass

    @abstractproperty
    def zoo_class(self):
        """ Return the classification of the Animal """
        pass

    def __init__(self, name = None):
        """ Set the default name to no name """
        if name:
            self.__name = name
        else:
            self.__name = "No name"

    def show(self):
        print("*"*40)
        print(f"Name: {self.name}")
        print(f'Number of legs: {self.legs}')
        print(f'Birth Type: {self.birth_type}')
        print(f'Zoological Classificaton: {self.zoo_class}')
        