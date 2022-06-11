import explorerhat

class Explora:

    __name = ""
    __speed = 100

    def __init__(self):
        """ Initialise the robot """
        self.__name = "Explora"
        explorer_hat = explorerhat

    @property
    def speed(self):
        """ Get the current speed"""
        return self.__speed

    @speed.setter
    def speed(self, value:int):
        if -100 < value < 100:
            self.__speed = value
        else:
            print('The speed must be an integer between -100 and 100')

    @property
    def name(self):
        """ Returns the robots name """
        return self.__name

    @name.setter
    def name(self, value:str):
        """ Sets the robots name """
        self.__name = value

    def forwards(self, speed:int=None):
        """ Move the robot forwards, 
        use the stop function to stop the robot """

        if speed is None:
            speed = self.__speed
        self.explorer_hat.motor.one.forwards(speed)
        self.explorer_hat.motor.two.backwards(speed)

    def backwards(self, speed:int=None):
        """ Move the robot backwards, 
        use the stop function to stop the robot """

        if speed is None:
            speed = self.__speed
        self.explorer_hat.motor.one.backwards(speed)
        self.explorer_hat.motor.two.forwards(speed)

    def turn_left(self, speed:int=None):
        """ Turn the robot left, 
        use the stop function to stop the robot """

        if speed is None:
            speed = 100
        self.explorer_hat.motor.one.forwards(speed)
        self.explorer_hat.motor.two.forwards(speed)

    def turn_right(self, speed:int=None):
        """ Turn the robot right, 
        use the stop function to stop the robot """

        if speed is None:
            speed = 100
        self.explorer_hat.motor.one.backwards(speed)
        self.explorer_hat.motor.two.backwards(speed)

    def stop(self):
        """ Stop the robot """
        self.explorer_hat.motor.one.stop)
        self.explorer_hat.motor.two.stop)

    def __ping(self):
        """ Returns the distance from the range finder """