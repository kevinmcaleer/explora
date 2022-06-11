``` mermaid
classDiagram
direction LR
    class Animal
    class Mammal 
    class Reptile 
    class Dog 
    class Cat 
    class Snake 
    class Insect 
    class Fly 

Animal <|-- Mammal
Animal <|-- Reptile
Mammal <|-- Dog
Mammal <|-- Cat
Reptile <|-- Snake
Animal <|-- Insect
Insect <|-- Fly
```