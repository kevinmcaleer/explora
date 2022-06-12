# Animals Demo
# Kevin McAleer
# June 2022

from cats import Cat
from dogs import Dog
from snake import Snake
from fly import Fly

# Create some animals
tigger = Cat('Tigger', breed="British Short Hair")
minnie = Dog('Minnie', breed="Chihuahua")
archie = Dog("Archie", breed="Chihuahua")
sid = Snake('Sid')
buz = Fly('Buzz')

# Put them in a list
animals = [tigger,minnie,sid, archie, buz]

# Display the details for each animal in the list
for animal in animals:

    animal.show()

