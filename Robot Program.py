#!/usr/bin/env python3

from ev3_bt_controller import *
from ev3dev.ev3 import *
import time



class Robot:

    def __init__(self):

        # self.us_f = UltrasonicSensor('in1')
        # self.us_r = UltrasonicSensor('in2')
        # self.us_l = UltrasonicSensor('in3')
        #
        # self.us_f.mode='US-DIST-CM'
        # self.us_r.mode='US-DIST-CM'
        # self.us_l.mode='US-DIST-CM'
        # self.units = self.us_f.units
        pass

    def step(self, n):
        '''
        n --> float | number of steps
        Makes the robot go forward for n steps (1 step = 27 cm).
        '''
        motors_step = [
            {
                'port': 1,
                'speed': -20,
                'duration': 2.1225
            },
            {
                'port': 4,
                'speed': -20,
                'duration': 2.1225
            }
        ]
        c = EV3_BT_Controller(motors_step)

        c.move_two_motors(motors_step)

    def turn_right(self, s=20,t=1.15):
        '''
        s --> float | engine speed
        t --> float | time working
        Makes the robot turn right.
        '''
        motors_turn1 = [
            {
                'port':1,
                'speed': -s,
                'duration': t,
            },
            {
                'port': 4,
                'speed': s,
                'duration': t,
            }
        ]
        EV3_BT_Controller(motors_turn1).move_two_motors(motors_turn1)

    def turn_left(self, s=20,t=1.15):
        '''
        s --> float | engine speed
        t --> float | time working
        Makes the robot turn left. 
        '''
        motors_turn2 = [
            {
                'port':1,
                'speed': s,
                'duration': t,
            },
            {
                'port': 4,
                'speed': -s,
                'duration': t,
            }
        ]
        EV3_BT_Controller(motors_turn2).move_two_motors(motors_turn2)

    def get_distances(self):
        '''
        Reads the Ultrasonic sensors of the robot.
        '''
        f = self.us_f.value()
        r = self.us_r.value()
        l = self.us_l.value()
        return (l,f,r)

    def print_values(self):
        '''
        Returns the US values to the user. 
        '''
        print(self.get_distances())

    def compare_distances(self):
        '''
        Makes the robot compare the distances around him, and choose to go towards the shortest distance.
        '''
        l,f,r = self.get_distances()
        if l < f and l < r:
            self.turn_left()
        elif r < f and r < l:
            self.turn_right()
        else:
            self.step(1)

my_robot = Robot()

# my_robot.step(2)
# time.sleep(2.5)
# my_robot.turn_right()
# my_robot.step(1)
# time.sleep(2.5)
# my_robot.turn_left()
# my_robot.get_distances(0)
# my_robot.print_values()

# us = UltrasonicSensor('ev3:in1')
# us.mode = 'US-DIST-CM'
# print(us.value())

print()