import RPi.GPIO as GPIO
import time
from gpiozero import AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()
servo = AngularServo(26, min_angle=-90, max_angle=90, pin_factory=factory)
PULX = 18
DIRX = 23

PULY = 24
DIRY = 25

def move_to(x0,y0,x1,y1):
    dx = abs(x1-x0) # how far horizantally
    dy = abs(y1-y0) # how far vertically
    
    # motor durections
    dir_x = 1 if x1 > x0 else -1 
    dir_y = 1 if y1 > y0 else -1

    error = dx-dy # how far off actual line.. Bresenham. positive error means X is ahead and vice versa
    x = x0
    y = y0
    
    if dir_x >= 0:
        GPIO.output(DIRX, GPIO.HIGH)
    else:
        GPIO.output(DIRX, GPIO.LOW)

    if dir_y >= 0:
        GPIO.output(DIRY, GPIO.HIGH)
    else:
        GPIO.output(DIRY, GPIO.LOW)
        
    while x != x1 or y != y1: # repeat until target met
        error2 = 2* error
        if error2 > -(dy):
            GPIO.output(PULX, GPIO.HIGH)
            time.sleep(0.001)
            GPIO.output(PULX, GPIO.LOW)
            time.sleep(0.001)
            x += dir_x
            error -= dy
            
        if error2 < (dx): 
            GPIO.output(PULY, GPIO.HIGH)
            time.sleep(0.001)
            GPIO.output(PULY, GPIO.LOW)
            time.sleep(0.001)
            y += dir_y
            error +=dx
            
def pen_up():

    servo.angle = -90
    time.sleep(0.2)
def pen_down():

    servo.angle = 30
    time.sleep(0.2)
    
def home(x0,y0):
    move_to(x0,y0,0,0)