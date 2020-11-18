#!/usr/bin/env python
"""
DEMO: Basis voor uitleg multiprocessing
"""

# IMPORTS
from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Button
import time


# AUTHOR INFORMATION
__author__ = "Thomas De Witte"
__email__ = "thomas.dewitte@kdg.be"
__status__ = "Development"


# CONFIGURING I/O - IP/LED/BUTTONS
IP = PiGPIOFactory(host='192.168.1.3')  # CHANGE IP TO YOUR RPI

LED_RAIL = LED(17, pin_factory=IP)  # LED ON RAIL IS PIN 17
LED_RAIL_2 = LED(19, pin_factory=IP)   # LED ON RAIL IS PIN 19
LED_WALL = LED(18, pin_factory=IP)  # LED ON WALL IS PIN 18

BUTTON_RAIL = Button(4, pin_factory=IP)  # BUTTON FOR LED RAIL IS PIN 4
BUTTON_WALL = Button(5, pin_factory=IP)  # BUTTON FOR LED RAIL IS PIN 5


# FUNCTIONS
def main():
    while True:
        turn_led_rails_on()
        turn_led_wall_on()


def turn_led_rails_on():
    if BUTTON_RAIL.is_held:  # FEATURE FROM USE CASE
        LED_RAIL.toggle()   # TURN THE LED ON OR OFF DEPENDING ON STATE
        LED_RAIL_2.toggle()    # THE SECOND LED FOLLOWS THE FIRST ONE
        time.sleep(5)
        LED_RAIL.off()   # TURN THE LED ON OR OFF DEPENDING ON STATE
        LED_RAIL_2.off()    # THE SECOND LED FOLLOWS THE FIRST ONE


def turn_led_wall_on():
    if BUTTON_WALL.is_held:  # FEATURE FROM USE CASE
        LED_WALL.toggle()   # TURN THE LED ON OR OFF DEPENDING ON STATE


if __name__ == '__main__':  # CODE TO EXECUTE IF CALLED FROM CLI
    main()

