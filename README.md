# Explora - the 3D printed robot you can build yourself

This is the code repository for the Explora robot.

clone this to your Raspberry Pi using the command:
`git clone https://github.com/kevinmcaleer/explora`

This will checkout the latest code for the Explora robot

Explora uses the [Pimoroni Explorer pHAT](https://shop.pimoroni.com/products/explorer-phat) to control the motors and provide the extra power required.

The Explorer pHat also comes with a Python Library that our code will use. To install this library type:

### Enable i2:
`sudo raspi-config nonint do_i2c 0

### Install the library:
`python -m pip install --upgrade explorerhat`

---

##  Files 
A list of the files provided in this respository are provided below:


File | Description
---|---
[`explora.py`](explora.py) | The Explora robot class
[`movement_demo.py`](movement_demo.py) | The main demo code
[`lessons`](lessons) | example code to demonstrate object oriented programming concepts
