from __future__ import print_function
from src.PincherArm import PincherArm
from time import sleep

try:
    # set up arm
    arm = PincherArm()
    # move arm straight up
    arm.init_arm()
    # scan for objects position
    scan_position = [150, 379, 511, 370, 511]
    # get in scan position
    for index, position in enumerate(scan_position):
        arm.move_servo(index + 1, position, arm.speed)
    # scan the area for objects
    for scan_angle in range(150, 1000, 50):
        arm.move_servo(1, scan_angle, arm.speed / 2.5)

    # import vision algo to scan
    # move to shut down position
    arm.shutdown_position()
    # kill power to arm
    arm.servos.turn_off()
except (KeyboardInterrupt, SystemExit):
    arm.servos.turn_off()
