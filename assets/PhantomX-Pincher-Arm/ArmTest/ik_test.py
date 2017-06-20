# /usr/bin/env/python3
# -*- coding: utf-8 -*-

from src.IK_engine import IK_engine as IK
from src.PincherArm import PincherArm
from time import sleep

# set up arm
arm = PincherArm()

x, y, z, tp, type = (0, -165, -125, 273, 2)
z -= 28

try:
    # move arm straight up
    arm.init_arm()

    ik = IK()
    error, angles = ik.calc_positions(t_x=x, t_y=y, t_z=z, g_a=tp, style=type)

    angles1 = ik.angle_2_servo_offset(angles)
    angles2 = [int(ik.deg_2_ax(deg)) for deg in angles1[:-1]] + [512]
    print('Moving arm to:', angles2)

    if not error:
        for index, position in enumerate(angles2):
            arm.move_servo(index + 1, position, arm.speed)

    sleep(5)
    arm.servos.turn_off()
except (KeyboardInterrupt, SystemExit):
    arm.servos.turn_off()