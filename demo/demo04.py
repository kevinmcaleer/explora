# Demo04 Car class
# Kevin McAleer
# 12 June 2022

# Car class

class Car:

    #  class properties
    __owner = "noone"
    __colour = "black"
    __fuel_type = "diesel"
    __model = "unknown"
    __engine_size = "unknown"
    __lights_status = False


    def __init__(self, owner=None, colour=None, fuel_type=None, model=None, engine_size=None):
        """ Create a new car """

        if owner: self.__owner = owner 
        if colour: self.__colour = colour
        if fuel_type: self.__fuel_type = fuel_type
        if model: self.__model = model
        if engine_size: self.__engine_size = engine_size


    @property
    def owner(self):
        """ Gets the owner of the car """
        return self.__owner

    @owner.setter
    def owner(self, value):
        """ Sets the owner of the car """
        if value in ['Stephen','John','Bill','Jane','Alex']:
            print("you cannot own this car")
        else:
            self.__owner = value

    def show_details(self):
        """ Show the car details """
        print(f"The {self.__colour} car is a {self.__fuel_type} powered {self.__model} and is owned by {self.__owner}")

    def lights_on(self):
        """ Turn the lights on """
        self.__lights_status = True
    
    def lights_off(self):
        """ Turn the lights off """
        self.__lights_status = False

    def lights_status(self):
        """ Show the current status of the lights """
        if self.__lights_status:
            print(f'The lights are on')
        else:
            print(f'The lights are off')

car1 = Car(owner="Stephen", colour="red", fuel_type="electric", model="Tesla", engine_size="80kW")

car1.show_details()
car1.lights_on()
car1.lights_status()
car1.lights_off()
car1.lights_status()