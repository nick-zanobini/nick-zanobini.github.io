# /usr/bin/env/python3
# -*- coding: utf-8 -*-

from src.IK_engine import IK_engine as IK

x, y, z, tp, type = (0, -215, -100, 300, 2)
correct_answer = [512, 685, 781, 587, 512]

ik = IK()
error, angles = ik.calc_positions(t_x=x, t_y=y, t_z=z, g_a=tp, style=type)
angles = [int(ang) for ang in angles]
# --------------------------------------------------------
# angles1 = ik.IK_2_servo(angles)
# angles1 = [int(ang) for ang in angles1]
# angles2 = ik.angle_2_servo_offset(angles1)
# angles2 = ik.legit_soln_check(angles2)
# print('The input angles are:       ', [x, y, z, tp])
# print('Calc Positions gives:       ', angles)
# print('IK to Servo gives:          ', angles1)
# print('Legit Solution Check gives: ', angles2)

# --------------------------------------------------------
angles2 = ik.angle_2_servo_offset(angles)
angles4 = [int(ik.deg_2_ax(deg)) for deg in angles2[:-1]]
print('The input angles are:       ', [x, y, z, tp])
print('Calc Positions gives:       ', angles)
print('Angle to Servo gives:       ', angles2)
print('angle2servo -> ax2deg:      ', angles4)
print('The correct solution is:    ', correct_answer)

# --------------------------------------------------------
angles1 = ik.IK_2_servo(angles)
angles1 = [int(ang) for ang in angles1]
angles2 = ik.angle_2_servo_offset(angles1)
angles3 = [int(ik.deg_2_ax(deg)) for deg in angles2[:-1]]
print('sequence             :      ', angles3)
print('The correct solution is:    ', correct_answer)

