import RPi.GPIO as GPIO
import time

# Real Robot Driver
class RealRobotDriver:
    def __init__(self):
        
        #GPIO Mode (BOARD / BCM)
        GPIO.setmode(GPIO.BCM)

        #set GPIO Pins for Sonar Sensors
        self.GPIO_LEFT_TRIGGER = 5
        self.GPIO_LEFT_ECHO = 6
        self.GPIO_RIGHT_TRIGGER = 17
        self.GPIO_RIGHT_ECHO = 27

        # set GPIO pins for motors
        self.GPIO_LEFT_MOTOR_SPEED = 12
        self.GPIO_LEFT_MOTOR_BLUE = 1
        self.GPIO_LEFT_MOTOR_ORANGE = 7
        self.GPIO_RIGHT_MOTOR_SPEED = 18
        self.GPIO_RIGHT_MOTOR_BLUE = 24
        self.GPIO_RIGHT_MOTOR_ORANGE = 23

        #set GPIO direction (IN / OUT)
        GPIO.setup(self.GPIO_LEFT_TRIGGER, GPIO.OUT)
        GPIO.setup(self.GPIO_LEFT_ECHO, GPIO.IN)
        GPIO.setup(self.GPIO_RIGHT_TRIGGER, GPIO.OUT)
        GPIO.setup(self.GPIO_RIGHT_ECHO, GPIO.IN)

        GPIO.setup(self.GPIO_LEFT_MOTOR_SPEED, GPIO.OUT)
        GPIO.setup(self.GPIO_LEFT_MOTOR_BLUE, GPIO.OUT)
        GPIO.setup(self.GPIO_LEFT_MOTOR_ORANGE, GPIO.OUT)
        GPIO.setup(self.GPIO_RIGHT_MOTOR_SPEED, GPIO.OUT)
        GPIO.setup(self.GPIO_RIGHT_MOTOR_BLUE, GPIO.OUT)
        GPIO.setup(self.GPIO_RIGHT_MOTOR_ORANGE, GPIO.OUT)

    def sonars(self):
        left_distance = self.sonar(self.GPIO_LEFT_TRIGGER, self.GPIO_LEFT_ECHO)
        right_distance = self.sonar(self.GPIO_RIGHT_TRIGGER, self.GPIO_RIGHT_ECHO)
        return left_distance, right_distance

    def sonar(self, GPIO_TRIGGER, GPIO_ECHO):
        # set Trigger to HIGH
        GPIO.output(GPIO_TRIGGER, True)

        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)

        StartTime = time.time()
        StopTime = time.time()

        # save StartTime
        while GPIO.input(GPIO_ECHO) == 0:
            StartTime = time.time()

        # save time of arrival
        while GPIO.input(GPIO_ECHO) == 1:
            StopTime = time.time()

        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2

        return distance
    
    def stop(self):
        GPIO.output(self.GPIO_LEFT_MOTOR_BLUE, GPIO.LOW)
        GPIO.output(self.GPIO_LEFT_MOTOR_ORANGE, GPIO.LOW)
        GPIO.output(self.GPIO_LEFT_MOTOR_SPEED, GPIO.LOW)
        GPIO.output(self.GPIO_RIGHT_MOTOR_BLUE, GPIO.LOW)
        GPIO.output(self.GPIO_RIGHT_MOTOR_ORANGE, GPIO.LOW)
        GPIO.output(self.GPIO_RIGHT_MOTOR_SPEED, GPIO.LOW)
        GPIO.output(self.GPIO_LEFT_TRIGGER, GPIO.LOW)
        GPIO.output(self.GPIO_RIGHT_TRIGGER, GPIO.LOW)

    def motor(self, velocity, speed_pin, blue_pin, orange_pin):
        if velocity == 0:
            GPIO.output(blue_pin, GPIO.LOW)
            GPIO.output(orange_pin, GPIO.LOW)
            GPIO.output(speed_pin, GPIO.LOW)
        elif velocity > 0:
            GPIO.output(blue_pin, GPIO.HIGH)
            GPIO.output(orange_pin, GPIO.LOW)
            GPIO.output(speed_pin, GPIO.HIGH)
        else:
            GPIO.output(blue_pin, GPIO.LOW)
            GPIO.output(orange_pin, GPIO.HIGH)
            GPIO.output(speed_pin, GPIO.HIGH)
    
    def motors(self, left, right, seconds):
        # Call real robot hardware control for left motor
        #self.robot_hardware.set_left_motor_speed(left)
        #self.robot_hardware.set_right_motor_speed(right)
        self.motor(left, self.GPIO_LEFT_MOTOR_SPEED, self.GPIO_LEFT_MOTOR_BLUE, self.GPIO_LEFT_MOTOR_ORANGE)
        self.motor(right, self.GPIO_RIGHT_MOTOR_SPEED, self.GPIO_RIGHT_MOTOR_BLUE, self.GPIO_RIGHT_MOTOR_ORANGE)
        time.sleep(seconds)
        self.stop()

    def exit(self):
        self.stop()
        return
