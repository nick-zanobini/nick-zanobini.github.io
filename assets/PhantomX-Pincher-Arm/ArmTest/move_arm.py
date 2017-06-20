from __future__ import print_function
from src.PincherArm import PincherArm
from time import sleep

try:
    # set up arm
    arm = PincherArm()
    # move arm straight up
    arm.init_arm()
    # scan for objects position
    move_position = [395, 471, 327, 454, 511]
    # get in scan position
    for index, position in enumerate(move_position):
        arm.move_servo(index + 1, position, arm.speed)
    while True:
        sleep(1)
except (KeyboardInterrupt, SystemExit):
    arm.servos.turn_off()

