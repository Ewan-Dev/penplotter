import lgpio
import time
from config import *
from gpiozero import AngularServo


h = lgpio.gpiochip_open(0)
lgpio.gpio_claim_output(h, PULX)
lgpio.gpio_claim_output(h, PULY)
lgpio.gpio_claim_output(h, DIRX)
lgpio.gpio_claim_output(h, DIRY)
PIXEL_TO_STEP_SCALE_FACTOR = 10

servo = AngularServo(SERVO_PIN)

def move_to(x0,y0,x1,y1):
    
    x0 *= PIXEL_TO_STEP_SCALE_FACTOR
    y0 *= PIXEL_TO_STEP_SCALE_FACTOR
    x1 *= PIXEL_TO_STEP_SCALE_FACTOR
    y1 *= PIXEL_TO_STEP_SCALE_FACTOR
    
    dx = abs(x1-x0) # how far horizantally
    dy = abs(y1-y0) # how far vertically
    
    # motor durections
    dir_x = 1 if x1 > x0 else -1 
    dir_y = 1 if y1 > y0 else -1

    error = dx-dy # how far off actual line.. Bresenham. positive error means X is ahead and vice versa
    x = x0
    y = y0
    
    lgpio.gpio_write(h, DIRX, 1 if dir_x >= 0 else 0)
    lgpio.gpio_write(h, DIRY, 1 if dir_y >= 0 else 0)
        
    while x != x1 or y != y1: # repeat until target met
        error2 = 2 * error
        if error2 > -dy and x != x1:
            lgpio.gpio_write(h, PULX, 1)
            time.sleep(0.0002)
            lgpio.gpio_write(h, PULX, 0)
            x += dir_x
            error -= dy
        if error2 < dx and y != y1:
            lgpio.gpio_write(h, PULY, 1)
            time.sleep(0.0002)
            lgpio.gpio_write(h, PULY, 0)
            y += dir_y
            error += dx
        time.sleep(STEP_DELAY)

def pen_up():

    servo.angle = -90
    time.sleep(0.2)
def pen_down():

    servo.angle = 30
    time.sleep(0.2)
    
def home(x0,y0):
    move_to(x0,y0,0,0)

def switch_pen(number, x0, y0):
    pen_down()
    if number == 1:
        move_to(x0,y0,0,20)
    elif number == 2:
        move_to(x0,y0,0,40)
    elif number == 3:
        move_to(x0,y0,0,60)
    elif number == 4:
        move_to(x0,y0,0,80)
    pen_up()

def place_pen_in_holder(number, x0, y0):
    pen_up()
    if number == 1:
        move_to(x0,y0,0,20)
    if number == 2:
        move_to(x0,y0,0,40)
    if number == 3:
        move_to(x0,y0,0,60)
    if number == 4:
        move_to(x0,y0,0,80)
    pen_down()
