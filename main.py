from ev3_bt_controller import *

motors = [
    {
        'port': 1,
        'speed': -100,
        'duration': .5
    },
    {
        'port': 4,
        'speed': -100,
        'duration': .5
    }
]
c = EV3_BT_Controller(motors)

c.move_two_motors(motors)

