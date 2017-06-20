from __future__ import print_function
from src.PincherArm import PincherArm
from time import sleep
import RPi.GPIO as GPIO
import sys
import os

# set up arm
arm = PincherArm()
# move arm straight up
arm.init_arm()
# get number of positions to record
print('How many positions do you want to record?')
num_of_positions = int(input('Number of Positions: '))
print('\n| --------------------------------------------------- |')
# create array to store all the positions
positions = []
joints = ['Base    ', 'Shoulder', 'Elbow   ', 'Wrist   ', 'Gripper ']
try:
    for position in range(num_of_positions):
        # create a temp array to store the positions
        temp = []
        print('| [INFO] Move the arm to the position you want it in. |')
        # kill power to arm
        arm.servos.turn_off()
        # wait until user is ready
        _ = input('| [INFO] Press Enter to continue:                     |')
        # power the arm
        arm.servos.turn_on()
        sleep(0.2)
        # read the value of all the servos
        for index, servo in enumerate([1, 2, 3, 4, 5]):
            # add servo locations to array
            temp.append(arm.servos.readPosition(servo))
        print('| [INFO] Storing servo locations for position %02d      |' % (position + 1))
        print('| --------------------------------------------------- |')
        # Store values of each servo in positions array
        positions.append(temp)

    print('')
    # print out servo locations for each positions
    for idx, position in enumerate(positions):
        print('              | --- Position {0:0>2} --- | '.format(idx + 1))
        for index, angle in enumerate(positions[idx]):
            print('              | {:s} angle: {:2d} |'.format(joints[index], angle))
    print('              | ------------------- | ')

except KeyboardInterrupt:
    pass
except Exception as e:
    print(str(e))
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)
finally:
    arm.servos.turn_off()
    GPIO.cleanup()
