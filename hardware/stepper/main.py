import RPi.GPIO as GPIO
import time
import json
import ast

from motor_tools import move_to, pen_up, pen_down, home
with open("image_code.txt", "r") as file:
    components = ast.literal_eval(file.read())

print(components)

PULX = 18
DIRX = 23

PULY = 24
DIRY = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(PULX, GPIO.OUT)
GPIO.setup(DIRX, GPIO.OUT)
GPIO.setup(PULY, GPIO.OUT)
GPIO.setup(DIRY, GPIO.OUT)
pen_up()

try:
    move_to(0, 0, components[0][0][0], components[0][0][1])
    for i, component in enumerate(components):
        print("NEW COMPONENT")
        pen_down()
        end_component_coords = None
        for j in range(0, len(component)-1):
            print(component[j])
            pixel_x = int(component[j][0])
            pixel_y = int(component[j][1])
            move_to(pixel_x, pixel_y, int(component[j+1][0]),  int(component[j+1][1]))
            end_component_coords = (int(component[j+1][0]),  int(component[j+1][1]))
        pen_up()
        if i == len(components) -1:
            home(end_component_coords[0], end_component_coords[1])
        else:
            move_to(end_component_coords[0], end_component_coords[1], components[i+1][0][0], components[i+1][0][1])
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()