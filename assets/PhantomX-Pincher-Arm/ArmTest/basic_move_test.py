from src.PincherArm import PincherArm
from time import sleep

# set up arm
arm = PincherArm()
# move arm straight up
arm.init_arm()
# wait 3 seconds
sleep(3)
# move arm to shutdown position
arm.shutdown_position()
# kill power to arm
arm.servos.turn_off()
