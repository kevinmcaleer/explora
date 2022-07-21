# Explora
# Kevin McAleer 
# May 2022

from time import sleep
from explora import Explora

robot = Explora()
robot.name = 'Kevs Robot'

speed = 50
while True:
  robot.forwards(speed)
  sleep(1)
  robot.stop()
  sleep(1)
  robot.turn_left(speed)
  sleep(0.5)
  robot.stop()
  sleep(1)
  robot.backwards(speed)
  sleep(1)
  robot.stop()
  sleep(1)
  robot.turn_right(speed)
  sleep(1)
  robot.stop()
  sleep(1)