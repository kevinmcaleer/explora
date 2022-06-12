# Demo03 A simple class
# Kevin McAleer
# 12 June 2022

# Cat class

class Cat:

    name = ""
    age = 0.0

    """ A simple class """
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        print(f"I am a cat, my name is {self.name} and I am {self.age} years old")

    def make_sound(self):
        print(f"{self.name} says Meow")


trixie = Cat(age= 16.0, name="Trixie")
cookie = Cat(age= 8.0, name="Cookie")
pepa = Cat(age= 2.0, name="Pepa")
bella = Cat(age= 1.0, name="Bella")
tigger = Cat(age= 0.6, name="Tigger")

trixie.info()
cookie.info()

tigger.make_sound()

