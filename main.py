# Import the robot control commands from the library
from simulator import robot
import time

#660x440

def stomp(direction):
    if direction== "right":
        robot.motors(1, -1, 0.76)
        robot.motors(1,1,0.5)
        robot.motors(-1,-1,0.5)
        robot.motors(1,1,0.5)
        robot.motors(-1,-1,0.5)
        robot.motors(-1,1,0.76)
    if direction== "left":
        robot.motors(-1, 1, 0.76)
        robot.motors(1,1,0.5)
        robot.motors(-1,-1,0.5)
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
    robot.motors(1,1,0.5)
    robot.motors(-1,-1,0.5)
    

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
    robot.motors(1,1,0.5)
    robot.motors(1,-1,1.5)

def chacha():
    left_distance, right_distance = robot.sonars()
    robot.motors(1,1,1.5)
    left_distance, right_distance = robot.sonars()
    robot.motors(1,1,1.5)
    left_distance, right_distance = robot.sonars()
    robot.motors(-1,-1,1.5)
    left_distance, right_distance = robot.sonars()
    robot.motors(-1,1,2)
    robot.motors(1,-1,2)
    if left_distance <5 and right_distance <5:
        robot.motors(-1,-1,0.5)  
    left_distance, right_distance = robot.sonars()
    if right_distance <5:
        robot.motors(-1,-1,0.5)
    robot.motors(-1,1,0.1)
    left_distance, right_distance = robot.sonars()
    if left_distance <5 and right_distance <5:
        robot.motors(-1,-1,0.5) 
    left_distance, right_distance = robot.sonars() 
    if right_distance <5:
        robot.motors(-1,-1,0.5)
    robot.motors(1,-1,1)
    left_distance, right_distance = robot.sonars()
    if left_distance <5 and right_distance <5:
        robot.motors(-1,-1,0.5)  
    left_distance, right_distance = robot.sonars()
    if right_distance <5:
        robot.motors(-1,-1,0.5)

def drebee(c):
    return "thanks for being an awesome teacher," +c +"! you've been the sweetest and genuinely make me excited to learn. let me know if you ever need to talk. i'm always here for you!! hope you have a great holiday break!"

def hello(b):
    return "hi "+b +"!"

p =input("are you ready to cha cha?")
o=input("are you sure?")
oo=input("is it time to get funky?")

while True:
    command = input("Command: ")
    if command == "exit":
        robot.exit()
    if command == "drebee":
        c=drebee(" Dr. Ebee")
        print(c)
    if command == "hi":
        name=hello("drebee")
        print(name)
    if command == "givemecoolgradetogetmeintocollegeplz":
        print(p)
        print(o)
        print(oo)
        print(o)
        print(p)
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
        hop()
        hop()
        stomp("right")
        stomp("left")
        knees() 
        getfunkywithit()
        chacha()
        






