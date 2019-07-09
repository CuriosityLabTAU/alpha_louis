#!/usr/bin/env python3
# so that script can be run from Brickman

from ev3dev.ev3 import *

# Connect ultrasonic and touch sensors to any sensor port
us = UltrasonicSensor(INPUT_1)

# Put the US sensor into distance mode.
us.mode='US-DIST-CM'