# Demo01 - without classes
# Kevin McAleer
# June 2022

from curses import beep

# Set the car colours
car01_colour = 'white'
car02_colour = 'grey'
car03_colour = 'duck egg blue'

# Set the car owners
car01_owner = 'Kev'
car02_owner = 'Jen'
car03_owner = 'Alex'

# Set the car models
car01_model = 'Zoe'
car02_model = 'A Class'
car03_model = '500'

# Set the car fuel type
car01_fuel_type = 'Electric'
car02_fuel_type = 'Petrol'
car03_fuel_type = 'Petrol'

# Set the engine size
car01_engine_size = "80kW"
car02_engine_size = "1.6l"
car02_engine_size = "1.0l"

def show_details(colour, owner, model, fuel):
    """ Show the car details"""
    print(f'The {colour} car is a {fuel} powered {model} and its owner is {owner}')

def beep_horn(car):
    """ Beep the car horn """
    print(f"car {car} beeps its horn")

def lights_on():
    """ Turn the lights on"""
    return True

def lights_off():
    """ Turn the lights off"""
    return False

def lights_status(car_lights):
    """ Show the current status of the headlights """
    if car_lights:
        print('Car lights are on')
    else:
        print('Car lights are off')

# Show car details
show_details(car01_colour, car01_owner, car01_model, car01_fuel_type)
show_details(car02_colour, car02_owner, car02_model, car02_fuel_type)
show_details(car03_colour, car03_owner, car03_model, car03_fuel_type)

# Beep the car horn
beep_horn('car01')

# Turn the headlights on an off
car01_lights = False
lights_status(car01_lights)
car01_lights = lights_on()
lights_status(car01_lights)