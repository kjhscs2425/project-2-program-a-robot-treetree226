# Import the robot control commands from the library
from simulator import robot
import time

left, right = robot.sonars()
robot.motors(1, 1, 2)
 