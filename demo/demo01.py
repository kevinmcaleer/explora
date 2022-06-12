# Demo01 without classes
# Kevin McAleer
# 12 June 2022

# Set the car colours
car01_colour = "white"
car02_colour = "grey"
car03_colour = "Duck Egg Blue"

# Set the car owners
car01_owner = "Kevin"
car02_owner = "Jen"
car03_owner = "Alex"

# Set the car models
car01_model = "Zoe"
car02_model = "A Class"
car03_model = "500"

# Set the car fuel types
car01_fuel_type = "Electric"
car02_fuel_type = "Petrol"
car03_fuel_type = "Diesel"

# Set the engine size
car01_engine_size = "80kW"
car02_engine_size = "1.6l"
car03_engine_size = "1.0l"

# Show Details
def show_details(colour, owner, model, fuel_type, engine_size):
    """ Shows the car details """
    print(f"The {colour} car is a {fuel_type} powered {model} and is owned by {owner}")

# Beep Horn
def beep_horn(car):
    """ 
    Beeps the horn 

    Doesn't return anything
    """
    print(f'car {car} beeps its horn')

# Lights On

def lights_on():
    return True

# Lights Off

def lights_off():
    return False 

# Lights Status
def lights_status(car_lights):
    """ Show the current status of the lights """
    if car_lights:
        print(f'The lights are on')
    else:
        print(f'The lights are off')

# show car details
show_details(car01_colour, car01_owner, car01_model, car01_fuel_type, car01_engine_size)
show_details(car02_colour, car02_owner, car02_model, car02_fuel_type, car02_engine_size)
show_details(car03_colour, car03_owner, car03_model, car03_fuel_type, car03_engine_size)

beep_horn('car01')

car01_lights = False
lights_status(car01_lights)
car01_lights = lights_on()
lights_status(car01_lights)