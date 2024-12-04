# Import the robot control commands from the library
from simulator import robot
import time

#660x440

#todo-make paramenter thingy for slide too

# left, right = robot.sonars()
# left=(-1, 1, 0.76)
# right=(1, -1, 0.76)

def stomp(direction):
    if direction== "right":
        robot.motors(1, -1, 0.76)
        robot.motors(1,1,0.5)
        robot.motors(-1,-1,0.5)
        robot.motors(-1,1,0.76)
    if direction== "left":
        robot.motors(-1, 1, 0.76)
        robot.motors(1,1,0.5)
        robot.motors(-1,-1,0.5)
        robot.motors(1,-1,0.76)

def rightstomp(): 
    robot.motors(1, -1, 0.76)
    robot.motors(1,1,0.5)
    robot.motors(-1,-1,0.5)
    robot.motors(-1,1,0.76)

def leftstomp(): 
    robot.motors(-1, 1, 0.76)
    robot.motors(1,1,0.5)
    robot.motors(-1,-1,0.5)
    robot.motors(1,-1,0.76)

def slide(direction1, direction2):
    robot.motors(direction1)
    robot.motors(1,1,0.5)
    robot.motors(-1,-1,0.5)
    robot.motors(direction2)

def slideleft(): 
    robot.motors(-1, 1, 1.52)
    robot.motors(1,1,0.5)
    robot.motors(-1,-1,0.5)
    robot.motors(1,-1,1.52)

def slideright():
    robot.motors(1,-1,1.52)
    robot.motors(1,1,0.5)
    robot.motors(-1,-1,0.5)
    robot.motors(-1,1,1.52)

def backnowyall():
    robot.motors(-1,-1,0.5)
    robot.motors(1,1,0.5)

def hop():
    robot.motors(1,1,0.25)
    robot.motors(-1,-1,0.25)
    robot.motors(1,1,0.25)
    robot.motors(-1,-1,0.25)

def chacha():
    robot.motors(1,-1,4)

def knees():
    robot.motors(-1, 1, 0.76)
    robot.motors(1,1,0.5)
    robot.motors(-1,-1,0.5)
    robot.motors(1, -1, 0.76)
    robot.motors(1,1,0.5)
    robot.motors(-1,-1,0.5)
    robot.motors(-1,1,1.52)

def funky():
    left_distance, right_distance = robot.sonars()
    if left_distance <10:
        pass
    if right_distance <10:
        pass


while True:
    command = input("Command: ")
    if command == "exit":
        robot.exit()
    else:
        left_distance, right_distance = robot.sonars()
        print(f"Left sonar is {left_distance} from the wall.")
        print(f"Right sonar is {right_distance} from the wall.")
        robot.motors(-1, 1, 1.52)
        left_distance, right_distance = robot.sonars()
        print(f"Left sonar is {left_distance} from the wall.")
        print(f"Right sonar is {right_distance} from the wall.")
        slideleft()
        backnowyall()
        hop()
        hop()
        stomp("right")
        stomp("right")
        stomp("left")
        stomp("left")
        knees()
        funky()
        chacha()
        






