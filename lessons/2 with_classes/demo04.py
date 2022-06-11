# Demo04 - with classes
# Kevin McAleer
# June 2022

class Car:

    # class properties
    _owner = 'noone'
    _colour = 'white'
    _fuel_type = 'Petrol'
    _engine_size = '2.0'
    _lights = False
    _model = 'Model-T Ford'

    def __init__(self, owner=None, colour=None, model=None, fuel_type=None, engine_size=None, lights=None):
        """ Create a new car """
        if owner: self._owner = owner
        if colour: self._colour = colour
        if fuel_type: self._fuel_type = fuel_type
        if engine_size: self._engine_size = engine_size
        if model: self._model = model

    @property
    def owner(self):
        """ Get the owner of the car """
        return self._owner
    
    @owner.setter
    def owner(self, value):
        """ Set the owner of the car """
        self._owner = value

    @property
    def colour(self):
        """ Get the colour of the car """
        return self._colour
    
    @colour.setter
    def colour(self, value):
        """ Set the colour of the car"""
        self._colour = value

    @property
    def fuel_type(self):
        """ Get the fuel type """
        return  self._fuel_type

    @fuel_type.setter
    def fuel_type(self, value):
        """ Set the fuel type """

        # check for value fuel type:
        if value in ['Petrol', 'Diesel', 'Electric', 'Hybrid']:
            self._fuel_type = value
        else:
            print("Invalid fuel type!")

    @property
    def engine_size(self):
        """ Get the engine size """
        return self._engine_size

    @engine_size.setter
    def engine_size(self, value):
        """ Set the engine size """
        self._engine_size = value

    @property
    def model(self):
        """ Get the car model """
        return self._model

    @model.setter
    def model(self, value):
        """ Set the cars model"""
        self._model = value

    def show_details(self):
        """ Display all the car's details """
        print(f'The {self._colour} car is a {self._fuel_type} powered {self._model} and its owner is {self._owner}')
    
    @property
    def lights(self):
        """ Get the Cars lights """
        if self._lights:
            print(f"{self._owner}'s lights are on")
        else:
            print(f"{self._owner}'s lights are off")

    @lights.setter
    def lights(self, value):
        """ Set the car lights """
        self._lights = value
    
    def lights_off(self):
        """ Turn the car lights off """
        self._lights = False

    def lights_on(self):
        """ Turn the car lights on """
        self._lights = True
        self.lights
    
    def beep_horn(self):
        """ Beep the cars horn """
        print('Beep Beep')

# Define the cars 
car01 = Car(owner='Kev', colour="White", fuel_type='Electric',engine_size='80kW', model='Zoe')
car02 = Car(owner='Jen', colour='Grey', engine_size='1.6l', fuel_type='Petrol', model='A Class')

# Show the details
car01.show_details()
car02.show_details()

# Lights and horn
car01.lights
car02.lights_on()
car02.beep_horn()
car01.lights
car02.lights

# change values
car01.fuel_type = 'red'
car01.fuel_type = 'Petrol'
car01.show_details()

car02.colour = 'Yellow'
car02.show_details()
