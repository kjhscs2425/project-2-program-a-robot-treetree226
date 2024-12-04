import pygame
import os
import numpy as np
import sys
import time

frame = 0
debug = False

def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(rho, phi)

def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)

class Robot:
    def __init__(self, use_simulator = True):
        if use_simulator:
            self.driver = SimulatorDriver()
        else:
            self.driver = RealRobotDriver()  # driver can be a simulator or real robot

    def motors(self, left, right, seconds):
        """Sends power to each wheel on the robot

        Parameters:
        * `left` power to the left motor (1 is forward, -1 is backward, 0 no power)
        * `right` power to the right motor (1, -1, 0)
        * `seconds` number of seconds (can be decimal)
        """
        self.driver.motors(left, right, seconds)
    
    def sonars(self):
        """Read from the sonar sensors
        
        Output: a tuple of the left and right distances from the sonar sensor to the nearest object in mm (or pixels)
        """
        return self.driver.sonars()
    
    def exit(self):
        self.driver.exit()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Simulator Driver
class SimulatorDriver:
    def __init__(self):
        self.origin = Point(300, 200)
        self.x = self.origin.x
        self.y = self.origin.y
        self.heading = 0 # pointing to the right
        self.left_motor_velocity = 0
        self.right_motor_velocity = 0
        self.radius = 20  # Robot radius for visualization
        self.robot_width = 200
        self.robot_height = 200
        size = 200
        self.img_left = pygame.image.load(os.path.join('img', "left", f"{size}", 'robobunny.png'))
        self.img_right = pygame.image.load(os.path.join('img', "right", f"{size}", 'robobunny.png'))
        self.img = self.img_left
        self.running = True
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.box_width = 660 #mm
        self.box_height = 410 #mm
        self.max_x_box = self.box_width / 2 + self.origin.x
        self.min_x_box = self.origin.x - self.box_width / 2
        self.max_y_box = self.box_height / 2 + self.origin.y
        self.min_y_box = self.origin.y - self.box_height / 2

        self.start_simulation()

    def find_corners(self, x, y, heading):
        """find right back corner, right front corner, left front corner, and left back corner, in that order"""
        i = np.array([1, 2, 3, 4])
        angle_to_corner = np.arctan(self.robot_width / self.robot_height)
        phi = heading - angle_to_corner
        omega = np.sqrt((self.robot_height / 2)**2 + (self.robot_width / 2)**2)
        corner_offsets = pol2cart(omega, phi + np.radians(90) * i)
        corner_x_values = x + corner_offsets[0]
        corner_y_values = y + corner_offsets[1]
        return corner_x_values, corner_y_values
    
    def detect_crash(self):
        corner_x_values, corner_y_values = self.find_corners(self.x, self.y, self.heading)
        biggest_x = np.max(corner_x_values)
        biggest_y = np.max(corner_y_values)
        smallest_x = np.min(corner_x_values)
        smallest_y = np.min(corner_y_values)
        x_crash = (biggest_x > self.max_x_box) or (smallest_x < self.min_x_box)
        y_crash = (biggest_y > self.max_y_box) or (smallest_y < self.min_y_box)
        return (x_crash or y_crash)

    def motors(self, left, right, seconds):
        # power (+ / -) to left and right motors
        # number of seconds to maintain that

        degrees_per_frame = 0.98

        # for a certain number of seconds:
        for _ in range(round(seconds * self.fps)):
            # update position
            if right == 1 and left == -1:
                self.heading = (self.heading - degrees_per_frame) % 360
            elif right == -1 and left == 1:
                self.heading = (self.heading + degrees_per_frame) % 360
            elif right == left:
                if right == 0:
                    pass
                else:
                    speed = right * 1
                    self.x += speed * np.cos(np.radians(self.heading))
                    self.y -= speed * np.sin(np.radians(self.heading))
            else:
                raise Exception("Ooops! Dr. Ebee didn't write code that let's you use those numbers as input to the `motors` function. If you *really* want those numbers, schedule some time on her calendar to help her implement that change!!")

            if self.detect_crash():
                raise Exception("Ooops! Dr. Ebee doesn't know how to simulate what happens when you hit the walls. Also, it's not good for the robot anyway. Try again!!")
            
            self.render()
    
    def dist_to_box(self, sonar_position, h):
        # from sonar position, draw a line in direction heading, and find distance to edge of box, which is:
        a = None
        b = None
        if 0 < h < 90:
            a = self.box_height - sonar_position.y
            b = self.box_width - sonar_position.x #distance to right
        elif 90 < h < 180:
            a = sonar_position.x #d to left
            b = self.box_height - sonar_position.y #d to top
        elif 180 < h < 270:
            a = sonar_position.y #d to bottom
            b = sonar_position.x #d to left
        elif 270 < h < 360:
            a = self.box_width - sonar_position.x #d to right
            b = sonar_position.y #d to bottom
        elif h == 0:
            return self.box_width - sonar_position.x
        elif h == 90:
            return self.box_height - sonar_position.y
        elif h == 180:
            return sonar_position.y
        elif h == 270:
            return sonar_position.x
        else:
            print(sonar_position.x, sonar_position.y)
        d = min(a / np.cos(h), b/ np.sin(h))
        return d

    def sonars(self):
        corners = self.find_corners(self.x, self.y, self.heading)
        left_front_corner = np.array([corners[0][0], corners[1][0]])
        right_front_corner = np.array([corners[0][-1], corners[1][-1]])
        v = right_front_corner - left_front_corner
        direction_vector = v / np.linalg.norm(v)
        left_sonar_position = left_front_corner + direction_vector * 3
        left_sonar_position = Point(left_sonar_position[0], left_sonar_position[1])

        v = left_front_corner - right_front_corner
        direction_vector = v / np.linalg.norm(v)
        right_sonar_position = right_front_corner + direction_vector * 3 
        right_sonar_position = Point(right_sonar_position[0], right_sonar_position[1])

        # draw a line between the front corners
        # sonar positions are 3cm in from the front corners

        # figure out distance from left sonar to box wall
        left_dist = self.dist_to_box(left_sonar_position, self.heading)
        # figure out distance from right sonar to box wall
        right_dist = self.dist_to_box(right_sonar_position, self.heading)
        return left_dist, right_dist

    def render(self):
        # Clear the screen
        self.screen.fill((255, 255, 255))

        # # keep bunny facing forward
        global frame
        frame += 1
        if debug and frame % 100 == 0:
            print(self.heading, np.cos(np.radians(self.heading)))
        if np.cos(np.radians(self.heading)) >= 0:
            self.img = pygame.transform.rotate(self.img_right, self.heading + 90)
        else:
            self.img = pygame.transform.rotate(self.img_left, self.heading - 90)

        rect = self.img.get_rect()
        rect.center = int(self.x), int(self.y)
        self.screen.blit(self.img, rect)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate to 60 FPS
        self.clock.tick(self.fps)

    def exit(self):
        print("Exiting simulation")
        self.running = False
        pygame.display.quit()
        pygame.quit()
        sys.exit()
        
    def start_simulation(self):
        # Initialize the Pygame window
        pygame.init()
        self.screen = pygame.display.set_mode((600, 400))
        pygame.display.set_caption("Robot Simulator")

mode = input("Do you want to run the real robot (r) or the simulator (s)?")
if mode == "r":
    from robot import RealRobotDriver
    robot = Robot(use_simulator=False)
    print("Robot simulation started!")
else:
    robot = Robot(use_simulator=True)
    print("Robot simulation started!")