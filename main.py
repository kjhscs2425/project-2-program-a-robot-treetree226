# Import the robot control commands from the library
from simulator import robot
import time

#660x440

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

def slide(direction):
    if direction== "right":
        robot.motors(1, -1, 1.52)
        robot.motors(1,1,0.5)
        robot.motors(-1,-1,0.5)
        robot.motors(-1,1,1.52)
    if direction== "left":
        robot.motors(-1, 1, 1.52)
        robot.motors(1,1,0.5)
        robot.motors(-1,-1,0.5)
        robot.motors(1,-1,1.52)

def backnowyall():
    robot.motors(-1,-1,0.5)
    robot.motors(1,1,0.5)

def hop():
    robot.motors(1,1,0.25)
    robot.motors(-1,-1,0.25)
    robot.motors(1,1,0.25)
    robot.motors(-1,-1,0.25)

def knees():
    robot.motors(-1, 1, 0.25)
    robot.motors(1,1,0.25)
    robot.motors(-1,-1,0.25)
    robot.motors(1, -1, 0.25)
    robot.motors(1,1,0.25)
    robot.motors(-1,-1,0.25)
    robot.motors(-1, 1, 0.25)
    robot.motors(1,1,0.25)
    robot.motors(-1,-1,0.25)
    robot.motors(1, -1, 0.25)
    robot.motors(1,1,0.25)
    robot.motors(-1,-1,0.25)
    robot.motors(-1, 1, 0.25)
    robot.motors(1,1,0.25)
    robot.motors(-1,-1,0.25)
    robot.motors(1, -1, 0.25)

def getfunkywithit():
    robot.motors(1,-1,2)

def chacha():
    left_distance, right_distance = robot.sonars()
    robot.sonars(-1,1,4)
    if left_distance <5:
        robot.sonars(-1,-1,180)
    if right_distance <5:
        robot.sonars(-1,-1,180)


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
        slide("left")
        backnowyall()
        hop()
        hop()
        stomp("right")
        stomp("right")
        stomp("left")
        stomp("left")
        knees()
        getfunkywithit()
        chacha()
        






