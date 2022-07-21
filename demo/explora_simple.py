import explorerhat

speed = 100   # the speed of the motors

explorer_hat = explorerhat

def forwards(new_speed:int=None):
    """ Move the robot forwards, 
    use the stop function to stop the robot """

    if new_speed is None:
        new_speed = speed
    explorer_hat.motor.one.forwards(new_speed)
    explorer_hat.motor.two.backwards(new_speed)

def backwards(new_speed:int=None):
    """ Move the robot backwards, 
    use the stop function to stop the robot """

    if new_speed is None:
        new_speed = speed
    explorer_hat.motor.one.backwards(new_speed)
    explorer_hat.motor.two.forwards(new_speed)

def turn_left(new_speed:int=None):
    """ Turn the robot left, 
    use the stop function to stop the robot """

    if new_speed is None:
        speed = 100
    explorer_hat.motor.one.forwards(new_speed)
    explorer_hat.motor.two.forwards(new_speed)

def turn_right(self, speed:int=None):
    """ Turn the robot right, 
    use the stop function to stop the robot """

    if speed is None:
        speed = 100
    explorer_hat.motor.one.backwards(speed)
    explorer_hat.motor.two.backwards(speed)

def stop(self):
    """ Stop the robot """
    explorer_hat.motor.one.stop()
    explorer_hat.motor.two.stop()

def ping(self):
    """ Returns the distance from the range finder """
    pass

""" Initialise the robot """
name = "Explora"
