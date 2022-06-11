# demo03
# Kevin McAleer
# June 2022

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


cat1 = Cat('Trixie', 16)
cat2 = Cat('Tigger', 0.6)

cat1.info()
cat2.info()

cat1.make_sound()