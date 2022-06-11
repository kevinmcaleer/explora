# Demo02 - without classes, dictionaries
# Kevin McAleer
# June 2022

from curses import beep

car01 = {'colour':'white', 'owner':'Kev', 'model':'Zoe', 'fuel_type':'Electric','engine_size':'80kW'}
car02 = {'colour':'grey', 'owner':'Jen', 'model':'A Class','fuel_type':'Petrol', 'engine_size':'1.6l'}
car03 = {'colour':'duck egg blue', 'owner':'Alex', 'model':'500','fuel_type':'Petrol', 'engine_size':'1.0l'}

def show_details(car):
    """ Show the car details"""
    print(f"The {car['colour']} car is a {car['fuel_type']} powered {car['model']} and its owner is {car['owner']}")

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
show_details(car01)
show_details(car02)
show_details(car03)

# Beep the car horn
beep_horn('car01')

# Turn the headlights on an off
car01_lights = False
lights_status(car01_lights)
car01_lights = lights_on()
lights_status(car01_lights)